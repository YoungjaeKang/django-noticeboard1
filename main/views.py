from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post, Member
from main.forms import PostForm
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth

from django.views import View
from django.views.generic import FormView
from . import forms, models
from django.urls import reverse_lazy

from django.contrib import messages


def index(request):
    return render(request, 'main/index.html')

# class LoginView(FormView):
#     """ Full Django Login """
#     template_name = "main/login.html"
#     form_class = forms.LoginForm
#     success_url = reverse_lazy("list")
#     # initial = {
#     #     'email': "hyunjin@naver.com"
#     # }

#     def form_valid(self, form):
#         email = form.cleaned_data.get("email")
#         password = form.cleaned_data.get("loginPw")
#         user = authenticate(self.request, username=email, password=password)
#         if user is not None:
#             login(self.request, user)
#         return super().form_valid(form)


def logout(request):
    auth.logout(request)
    return redirect('home')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, 'username or password is incorrect')
            return render(request, 'main/login.html')
    else:
        return render(request, 'main/login.html')

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         # loginId = request.POST['loginId']
#         username = request.POST['email']
#         password = request.POST['loginPw']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect('/main/list/')
#         else:
#             return HttpResponse('로그인 실패. 다시 시도해 보세요.')
#     else:
#         form = LoginForm()
#         return render(request, 'main/login.html', {'form': form})
#     # return render(request, 'main/login.html')


def join(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"],
            )
            auth.login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.INFO, '비밀번호가 일치하지 않습니다.')
            return render(request, 'main/join.html', )
    return render(request, 'main/join.html')


# def join(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             new_item = form.save()
#         return HttpResponseRedirect('/main/list/')
#     form = MemberForm()
#     return render(request, 'main/join.html', {'form':form})


def board(request):
    return render(request, 'main/board.html')


def list(request):
    postAll = Post.objects.all()    
    paginator = Paginator(postAll, 5)    
    page = request.GET.get('page')
    postAll = paginator.get_page(page)

    context = {
        'postAll': postAll,
    }
    return render(request, 'main/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/main/list/')
    form = PostForm()
    return render(request, 'main/create.html', {'form':form})

def detail(request, id):
    # TODO: 게시물 찍고 들어갔을 때 상세 화면 구현
    if 'id' is not None:
        item = get_object_or_404(Post, pk=id)
        # reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'main/detail.html', {'item': item})
    return HttpResponseRedirect('main/list/')


def delete(request):
    # TODO: 게시물 찍고 들어갔을 때 삭제 기능 구현
    # TODO: 게시글 지우거나 수정할 때 비밀번호 입력
    pass


def update(request):
    # TODO: 게시물 찍고 들어갔을 때 수정 기능 구현
    # TODO: 게시글 지우거나 수정할 때 비밀번호 입력
    pass