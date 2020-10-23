from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def Homepage(request):
	return render(request,"homepage.html")

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form= UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
def htmltutorials(request):
    return render(request,"htmltutorials.html")
def htmltutorialsbasictags(request):
    return render(request,"htmltutorials-basictags.html")
def csstutorials(request):
    return render(request,"csstutorials.html")
def csstutorialssyntax(request):
    return render(request,"css_syntax.html")
def csstutorialsselectors(request):
    return render(request,"css_selectors.html")
def csstutorialscomments(request):
    return render(request,"css_comments.html")
def csstutorialsborders(request):
    return render(request,"css_borders.html")
def csstutorialsmargins(request):
    return render(request, "css_margins.html")
def csstutorialsboxmodel(request):
    return render(request, "css_boxmodel.html")
def csstutorialsposition(request):
    return render(request, "css_position.html")
def csstutorialspseudoelements(request):
    return render(request, "css_pseudoelements.html")
def csstutorialstransitions(request):
    return render(request, "css_transitions.html")
def csstutorialsanimations(request):
    return render(request, "css_animations.html")

def htmltutorialstextformatting(request):
    return render(request,"htmltutorials-textformatting.html")
def htmltutorialscitationtags(request):
    return render(request,"htmltutorials-citationtags.html")


