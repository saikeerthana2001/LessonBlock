from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def Homepage(request):
	return render(request,"homepage.html")

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Homepage')
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
def jstutorials(request):
    return render(request,"jstutorials.html")
def jstutorialsoutput(request):
    return render(request,"js_output.html")
def jstutorialsstatements(request):
    return render(request,"js_statements.html")
def jstutorialssyntax(request):
    return render(request, "js_syntax.html")
def cssexamples(request):
    return render(request,"css_examples.html")
def htmltutorialslists(request):
    return render(request,"htmltutorials-lists.html")
def htmltutorialstables(request):
    return render(request,"htmltutorials-tables.html")
def htmltutorialsblocklevel(request):
    return render(request,"htmltutorials-blocklevel.html")
def htmltutorialsinline(request):
    return render(request,"htmltutorials-inline.html")
def htmltutorialsforms(request):
    return render(request,"htmltutorials-forms.html")
def jstutorialscomments(request):
    return render(request, "js_comments.html")
def jstutorialsarithmetic(request):
    return render(request,"js-arithmetic.html")
def jstutorialsfunctions(request):
    return render(request,"js_func.html")
def jstutorialsarrays(request):
    return render(request,"js_arrays.html")
def cssreferences(request):
    return render(request,"css_references.html")
def htmlexamples(request):
    return render(request,"htmlexamples.html")
def htmlreferencesss(request):
    return render(request,"htmlreferences.html")
def jsexamples(request):
    return render(request,'jsexamples.html')
def jsreferences(request):
    return render(request,'jsreferences.html')
def cssex1(request):
    return render(request,'css_ex1.html')






