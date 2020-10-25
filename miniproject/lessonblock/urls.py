
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
    path('jstutorials/',jstutorials,name="jstutorials"),
    path('jstutorials/output',jstutorialsoutput,name="jstutorials-output"),
    path('jstutorials/statements',jstutorialsstatements,name="jstutorials-statements"),
    path('jstutorials/syntax',jstutorialssyntax,name='jstutorials-syntax'),
    path('cssexamples/',cssexamples,name="cssexamples"),
    path('htmltutorials/lists',htmltutorialslists,name='htmltutorials-lists'),
    path('htmltutorials/tables',htmltutorialstables,name='htmltutorials-tables'),
    path('htmltutorials/blocklevel',htmltutorialsblocklevel,name='htmltutorials-blocklevel'),
    path('htmltutorials/inline',htmltutorialsinline,name='htmltutorials-inline'),
    path('htmltutorials/forms',htmltutorialsforms,name='htmltutorials-forms'),
    path('jstutorials/comments',jstutorialscomments,name="jstutorials-comments"),
    path('jstutorials/arithmetic',jstutorialsarithmetic,name="jstutorials-arithmetic"),
    path('jstutorials/functions',jstutorialsfunctions,name="jstutorials-functions"),
    path('jstutorials/arrays',jstutorialsarrays,name="jstutorials-arrays"),
]
