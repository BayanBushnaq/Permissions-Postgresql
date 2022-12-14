from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView , RetrieveUpdateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer , CommentSerializer
from .models import Book , ReadersComments
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny , IsAuthenticatedOrReadOnly
class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes = [IsOwnerOrReadOnly]

class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[IsOwnerOrReadOnly]


class CommentListView(ListCreateAPIView):
    queryset = ReadersComments.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsOwnerOrReadOnly]

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ReadersComments.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsOwnerOrReadOnly]