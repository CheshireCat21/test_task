import re
from message.models import Message
from message.serializer import MessageSerializer
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        block_number = self.request.parser_context['kwargs']['block_number']
        return Message.objects.all()[block_number * 10:block_number * 10 + 10]


class MessageRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
