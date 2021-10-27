from rest_framework import serializers

from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    text = serializers.CharField(max_length=99, min_length=1)

    class Meta:
        model = Message
        fields = '__all__'
