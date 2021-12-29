
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('test/' , views.test , name ='test'),
    path('add' , views.add , name ='add'),
    path('formpost' , views.formPost , name='formPost') ,
    path('addpost' , views.addPost , name='formPost') 
]
