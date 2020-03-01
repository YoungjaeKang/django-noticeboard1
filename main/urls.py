from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signin/', views.signin, name="signin"),
    # path("login/", views.LoginView.as_view(), name="login"),
    path('list/', views.list, name="list"),
    path('board/', views.board, name="board"),
    path('post/<int:id>', views.detail, name='post-detail'),
    path('create/', views.create, name='create'),
    path('join/', views.join, name='join'),
]