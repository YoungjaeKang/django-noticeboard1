from django.forms import ModelForm
from django import forms
from main.models import Post, Member
from django.utils.translation import gettext_lazy as _



# TODO: 어떻게 하면 detail, create, update form을 통일할 수 있을까?
class LoginForm(ModelForm):
    class Meta:
        model = Member
        fields = [
            'loginId',
            'loginPw',
        ]


class MemberForm(ModelForm):
    # TODO: 비밀번호 일치 확인 기능 넣기
    class Meta:
        model = Member
        fields = [
            'name',
            'loginId',
            'loginPw',
            'email',
        ]
        widgets = {
            'loginPw': forms.PasswordInput()
        }
        labels = {
            'name': _('이름'),
            'loginId': _('아이디'),
            'loginPw': _('비밀번호'),
            'email': _('이메일'),
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