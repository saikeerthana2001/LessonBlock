
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
    path('csstutorials/',csstutorials,name="csstutorials"),
    path('csstutorials/syntax',csstutorialssyntax,name='csstutorials-syntax'),
    path('csstutorials/selectors',csstutorialsselectors,name='csstutorials-selectors'),
    path('csstutorials/comments',csstutorialscomments,name='csstutorials-comments'),
    path('csstutorials/borders',csstutorialsborders,name='csstutorials-borders'),
    path('csstutorials/margins',csstutorialsmargins,name='csstutorials-margins'),
    path('csstutorials/boxmodel',csstutorialsboxmodel,name='csstutorials-boxmodel'),
    path('csstutorials/position',csstutorialsposition,name='csstutorials-position'),
    path('csstutorials/pseudoelements',csstutorialspseudoelements,name="csstutorials-pseudoelements"),
    path('csstutorials/transitions',csstutorialstransitions,name="csstutorials-transitions"),
    path('csstutorials/animations',csstutorialsanimations,name="csstutorials-animations"),

]
