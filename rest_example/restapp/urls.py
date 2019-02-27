from django.contrib import admin
from django.urls import path

from restapp.views import UserDetail,UserList
urlpatterns = [
    path('users/',UserList.as_view()),
    path('userdetails/<int:pk>',UserDetail.as_view()),
]