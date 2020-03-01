from django.forms import ModelForm
from django import forms
from . import models
from main.models import Post, Member
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("loginPw")
        try:
            user = models.Member.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))

        except models.Member.DoesNotExist:
            self.add_error("email",forms.ValidationError("User does not exist"))

# class LoginForm(ModelForm):
#     class Meta:
#         model = Member
#         fields = [
#             'email',
#             'loginPw',
#         ]
#         labels = {
#             'email': _('email'),
#             'password': _('password'),
#         }


class MemberForm(ModelForm):
    # TODO: 비밀번호 일치 확인 기능 넣기
    class Meta:
        model = Member
        fields = [
            'name',
            'email',
            'loginPw',
        ]
        widgets = {
            'loginPw': forms.PasswordInput()
        }
        labels = {
            'name': _('username'),
            'loginPw': _('password'),
            'email': _('email'),
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'contents',
            'writer',
            'created',
        ]
        labels = {
            'title': _('제목'),
            'contents': _('내용'),
            'writer': _('작성자'),
            # TODO: 작성자에는 로그인한 사람이 와야 한다.
        }
        error_messages = {
            'title': {
                'max_length': _('제목이 너무 길어요. 50자 이하로 해주세요.')
            },
            'contents': {
                'max_length': _('내용이 너무 길어요. 500자 이하로 해주세요.')
            },
        }