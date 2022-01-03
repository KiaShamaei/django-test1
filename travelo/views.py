from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def travelo(request):
    dest1 = Destination()
    dest1.name= "kia"
    dest1.desc = "is very smart person"
    dest1.img = "customer1.jpeg"
    dest1.price = 7000
    dest1.offer = True
    dest2 = Destination()
    dest2.name= "ahmad"
    dest2.desc = "is very smart young"
    dest2.img = "customer2.jpeg"
    dest2.price = 6500
    dest2.offer = False
    dest3 = Destination()
    dest3.name= "kia"
    dest3.desc = "is very smart big"
    dest3.img = "customer3.jpeg"
    dest3.price = 5000
    dest3.offer = False
    dests = [dest1,dest2,dest3]
    return render(request, 'index.html' , {'dests' : dests} )