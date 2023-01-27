from django.db import models 
import re 
from apps.login_reg.models import *
 
# create your models here 
# Field Types Link: https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types 

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be more than 2 characters"
        if len(postData['desc']) < 5:
            errors['desc'] = "Description must be at least 5 characters long if used, but it is optional"
        return errors

    def new_book(self, postData, uploader):
        thisBook = Book.objects.create(title = postData['title'], desc=postData['desc'], uploader = uploader)
        return thisBook




class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploader = models.ForeignKey('login_reg.User', related_name="books_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField('login_reg.User', related_name="books_liked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()









