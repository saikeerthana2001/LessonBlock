
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import *

urlpatterns = [
    path('',Homepage,name='Homepage'),
    path('signup/',signup,name='signup'),
]
