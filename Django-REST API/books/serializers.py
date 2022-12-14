from rest_framework import serializers
from .models import Book , ReadersComments
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        # fields = ['id','name','Auther','Number_of_pages']
        fields = '__all__'



# CommentSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReadersComments
        # fields = ['id','name','Auther','Number_of_pages']
        fields = '__all__'

