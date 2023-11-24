from rest_framework import serializers
from .models import Book_modle




class BookstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_modle
        fields = '__all__'



