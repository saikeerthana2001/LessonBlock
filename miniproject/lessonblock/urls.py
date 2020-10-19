
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import *

urlpatterns = [
    path('',Homepage,name='Homepage'),
    path('signup/',signup,name='signup'),
    path('htmltutorials/',htmltutorials,name='htmltutorials'),
    path('htmltutorials/basictags',htmltutorialsbasictags,name='htmltutorials-basictags'),
    path('htmltutorials/textformatting',htmltutorialstextformatting,name='htmltutorials-textformatting'),
    path('htmltutorials/citationtags',htmltutorialscitationtags,name='htmltutorials-citationtags'),
]
