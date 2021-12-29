
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('test/' , views.test , name ='test'),
    path('add' , views.add , name ='add')
]
