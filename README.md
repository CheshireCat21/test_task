GenericViews are used for we do not have complex logic in our views

Besides, if I write something more complicated I prefer to create new service directory (as a module) 
and put my business logic there.




Example of Using EMAIL_REGEX
```python
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class MessageRetrieveView(RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def patch(self, request, id):
        message = Message.objects.get(id=id)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            text = serializer.validated_data['text']
            if not re.match(EMAIL_REGEX, email) or len(text) >= 100:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```