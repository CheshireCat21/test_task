import re

from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from message.models import Message
from message.serializer import MessageSerializer


EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, block_number):
        messages = Message.objects.all()[block_number * 10:block_number * 10 + 10]
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class MessageSingleView(RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, id):
        message = Message.objects.get(id=id)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def patch(self, request, id):
        message = Message.objects.get(id=id)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            text = serializer.validated_data['text']
            if not re.match(EMAIL_REGEX, email) or len(text) > 100:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            text = serializer.validated_data['text']
            if not re.match(EMAIL_REGEX, email) or len(text) > 100:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
