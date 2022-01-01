from django.urls import path
from . import views

urlpatterns = [
    path('', views.travelo , name='home'),
]
