from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    Auther = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Number_of_pages = models.CharField(max_length=255)
    Available = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ReadersComments(models.Model):
    comment = models.CharField(max_length=255)
    Auther = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    
    

    def __str__(self):
        return self.comment