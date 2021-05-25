from django.http import HttpResponse
from django.shortcuts import render  #might have to remove later

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def new(request):
    return HttpResponse('New Products')