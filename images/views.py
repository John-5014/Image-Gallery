import datetime as dt 
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.

def index(request):
  return render(request,'index.html')

def images_of_day(request):
  date =dt.date.today()
  return render(request,'all-images/today-images.html', {"date":date,})



  
