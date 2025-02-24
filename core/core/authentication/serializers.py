from rest_framework import serializers
from .models import Book
from .models import Message

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= Message
        fields = '__all__'