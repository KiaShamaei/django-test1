from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def travelo(request):
    dest1 = Destination()
    dest1.name= "kia"
    dest1.desc = "is very smart person"
    dest1.price = 7000
    return render(request, 'index.html' , {'dest1' : dest1} )