
from django.urls import path
from .views import BookListView,BookDetailView , CommentListView , CommentDetailView
urlpatterns = [
    path('',BookListView.as_view(),name='book_list'),
    path('<int:pk>', BookDetailView.as_view(),name='book_detail'),
    path('Comments/',CommentListView.as_view(),name='Comment_list'),
    path('Comments/<int:pk>', CommentDetailView.as_view(),name='Comment_detail'),
    
]
