from django.shortcuts import render
from django.views import generic

from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse("Cia yra examination")
