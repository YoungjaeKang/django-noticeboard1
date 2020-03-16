import os
from uuid import uuid4
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, null=True)
    contents = models.TextField(null=True)
    writer = models.CharField(max_length=30, null=True)
    created = models.DateField(default=timezone.now(), null=True)
    photo = models.ImageField(blank=True, upload_to='post/%Y/%m/%d') # upload_to는 문자열 또는 함수 반환
    # category tag로 코딩
    # photo = models.ImageField()
    
    def __str__(self):
        return self.title

    # uuid를 통한 이미지 파일 저장하기 (파일명 정하기)
    # uuid4.hex 를 실행하면 32자리 난수를 만들어준다
    def uuid_name_upload_to(instance, filename):
        app_label = instance.__class__._meta.app_label  # 앱 별로
        acls_name = instance.__class__.__name__.lower() # 모델 별로
        ymd_path = timezone.now().strftime('%Y/%m/%d')  # 업로드하는 년/월/일 별로
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출하고 소문자로 변환
        return '/'.join([
            app_label,
            acls_name,
            ymd_path,
            uuid_name[:2],
            uuid_name + extension,
        ])


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
