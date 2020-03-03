from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    contents = models.TextField(null=True)
    writer = models.CharField(max_length=30, null=True)
    created = models.DateField(default=timezone.now(), null=True)
    # category tag로 코딩
    # photo = models.ImageField()
    
    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=50, null=True)
    # loginId = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    loginPw = models.CharField(max_length=50, null=True)    # pw filed로 바꾸기

    def __str__(self):
        return self.name


class Review(models.Model):
    comment = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created = models.DateField(default=timezone.now(), null=True)
