from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Time is precious")
# Create your views here.
