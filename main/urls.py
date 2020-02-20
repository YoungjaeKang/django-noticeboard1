from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('list/', views.list, name="list"),
    path('board/', views.board, name="board"),
    path('detail/', views.detail, name="detail"),
]