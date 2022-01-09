from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def travelo(request):
    dests = Destination.objects.all()
    return render(request, 'index.html' , {'dests' : dests} )