from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.utils.timezone import datetime

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
def cssex2(request):
    return render(request,'css_ex2.html')
def cssex3(request):
    return render(request,'css_ex3.html')
def cssex4(request):
    return render(request,'css_ex4.html')
def cssex5(request):
    return render(request,'css_ex5.html')
def htmlex1(request):
    return render(request,"html_ex1.html")
def htmlex2(request):
    return render(request,"html_ex2.html")
def htmlex3(request):
    return render(request,"html_ex3.html")
def htmlex4(request):
    return render(request,"html_ex4.html")
def htmlex5(request):
    return render(request,"html_ex5.html")
def jsex1(request):
    return render(request,"js_ex1.html")
def jsex2(request):
    return render(request,"js_ex2.html")
def jsex3(request):
    return render(request,"js_ex3.html")
def jsex4(request):
    return render(request,"js_ex4.html")
def jsex5(request):
    return render(request,"js_ex5.html")
def onlinecompiler(request):
    return render(request,"onlinecompiler.html")
@login_required(login_url="/signup/")
def certification(request):
    return render(request,'certification.html')
@login_required(login_url="/signup/")
def htmlexam(request):
    return render(request,'htmlexam.html')
@login_required(login_url="/signup/")
def cssexam(request):
    return render(request,'cssexam.html')

@login_required(login_url="/signup/")
def jsexam(request):
    return render(request,'jsexam.html')

@login_required(login_url="/signup/")
def frontendexam(request):
    return render(request,'frontendexam.html')


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




# Opens up page as PDF
class ViewPDF1(View):
    def get(self, request, *args, **kwargs):
        data={
            'today':datetime.today().strftime("%d/%m/%Y"),
            'name':request.user.username,
            'subject': 'HTML',
        }
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Opens up page as PDF
class ViewPDF2(View):
    def get(self, request, *args, **kwargs):
        data={
            'today':datetime.today().strftime("%d/%m/%Y"),
            'name':request.user.username,
            'subject': 'CSS',
        }
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Opens up page as PDF
class ViewPDF3(View):
    def get(self, request, *args, **kwargs):
        data={
            'today':datetime.today().strftime("%d/%m/%Y"),
            'name':request.user.username,
            'subject': 'Javascript',
        }
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
# Opens up page as PDF
class ViewPDF4(View):
    def get(self, request, *args, **kwargs):
        data={
            'today':datetime.today().strftime("%d/%m/%Y"),
            'name':request.user.username,
            'subject': 'Front-End',
        }
        pdf = render_to_pdf('pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')












