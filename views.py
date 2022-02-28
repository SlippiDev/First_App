from urllib import request
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
def home(request):
    return HttpResponse('Hi There!')
# Create your views here
def greeting(request):
    return HttpResponse('Greetings to all of you!')
def ashank(request):
    return HttpResponse('Hi, this is Ashank.')
def hellothere(request):
    return render(request,'FirstApp/hello_there.html')
def hellothere1(request,name):
    return render(request, 'FirstApp/hellothere1.html', {'name':name})
def calc(request):
    return render(request, 'FirstApp/MyTripleCalculator.html')
def style(request):
    return render(request, 'FirstApp/withstyle.html')
def website1(request):
    return render(request, 'FirstApp/javaslide_webprac.html')
def pm(request):
    return render(request, 'FirstApp/principal_message.html')
def vm(request):
    return render(request, 'FirstApp/VP_message.html')
def robotics(request):
    return render(request, 'FirstApp/robotics_intro.html')
def hostel(request):
    return render(request, 'FirstApp/hostel_facility.html')
def scripting(request):
    from random import choice
    nums = [1,2,3,4,5,6]
    a = choice(nums)
    context = {'number':a}
    return render (request,  'FirstApp/python1.html', context)
def getpdf(request):
    path = 'FirstApp/static/FirstApp/media/0025_211025185951_001.pdf'
    filename = 'ab.pdf'
    path1 = open(path, 'rb')
    mime_type, _ = mimetypes.guess_type(path)
    response = HttpResponse(path1, content_type = mime_type)
    response['Content-Deposition'] = "attachment; filename = %s"%filename  
    return response
from .forms import StudentFormUpload, formcontactform
from .functions import handle_uploaded_file
def upload(request):
    if request.method == 'POST':
        student = StudentFormUpload(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['files'])
            return HttpResponse('File Uploaded Successfully.')
    else:
        student = StudentFormUpload()
    return render(request, "FirstApp/form1.html", {'form':student}) 
def showform(request):
    form = formcontactform(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form} 
    return render(request, 'FirstApp/contactform1.html', context)
from .models import contactform1
from django.shortcuts import render
def display(request):
    st = contactform1.objects.all()
    return render(request, 'FirstApp/displaydata.html', {'st':st})