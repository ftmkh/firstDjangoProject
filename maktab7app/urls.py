from django.contrib import admin
from django.urls import path
from . import views

app_name = 'maktab7app'
urlpatterns = [
    path('', views.home , name='home' ),
    path('blogs', views.bolgs , name='blogs' ),
    path('<str:author>', views.bolgs , name='blogs' ),
    path('blogs/<str:post_title>', views.single_blog, name='title' )
]
