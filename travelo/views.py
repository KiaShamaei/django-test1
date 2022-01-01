from django.shortcuts import render
from django.http import HttpResponse

def travelo(request):
    return render(request, 'index.html' )