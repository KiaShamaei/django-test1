from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html' , {'name' : "hassan"})
def test(request):
    return HttpResponse("<h2>this is test ----</h2>")