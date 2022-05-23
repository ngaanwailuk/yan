from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request,'index.html') 
def brew_guide(request):
     return render(request,'brew-guide.html') 
def partnerships(request):
     return render(request,'partnerships.html') 
def ourstory(request):
     return render(request,'ourstory.html') 
