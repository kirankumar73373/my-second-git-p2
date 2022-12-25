from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def raju(request):
    return HttpResponse('<marquee>raju is a youth icon star</marquee>')

def ashrith(request):
    return HttpResponse('ashrith is a worst guy in the world')
