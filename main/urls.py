from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('list/', views.list, name="list"),
    path('board/', views.board, name="board"),
    path('post/<int:id>', views.detail, name='post-detail'),
    path('create/', views.create, name='create'),

]