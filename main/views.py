from django.shortcuts import render


def login(request):
    return render(request, 'main/login.html')


def list(request):
    return render(request, 'main/list.html')


def board(request):
    return render(request, 'main/board.html')