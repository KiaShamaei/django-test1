from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html' , {'name' : "hassan"})
def test(request):
    return HttpResponse('<h1>this is a test page </h2>')
def formPost(request):
    return render(request, 'formPost.html' )
def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2
    return render(request , 'result.html'  , {'result' : result})
def addPost(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 + val2
    return render(request , 'result.html'  , {'result' : result})