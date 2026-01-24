from rest_framework import serializers
from .models import Book, Game

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'release', 'completion', 'start']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'hours_played', 'release', 'completion', 'start']