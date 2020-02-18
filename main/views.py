from django.shortcuts import render
from main.models import Post, Member
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

def login(request):
    # TODO: Member를 통한 Login 기능 구현
    # TODO: 회원가입 기능 구현
    return render(request, 'main/login.html')

def board(request):
    return render(request, 'main/board.html')


def list(request):
    postAll = Post.objects.all()
    
    # TODO: 페이지네이션 구현
    # paginator = Paginator(postAll, 5)    
    # page = request.GET.get('page')
    # postAll = paginator.get_page(page)

    context = {
        'postAll': postAll,
    }
    return render(request, 'main/list.html', context)


def detail(request):
    # TODO: 게시물 찍고 들어갔을 때 상세 화면 구현
    pass

def delete(request):
    # TODO: 게시물 찍고 들어갔을 때 삭제 기능 구현
    # TODO: 게시글 지우거나 수정할 때 비밀번호 입력
    pass

def update(request):
    # TODO: 게시물 찍고 들어갔을 때 수정 기능 구현
    # TODO: 게시글 지우거나 수정할 때 비밀번호 입력
    pass