from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def thamana(request):
    return HttpResponse('<marquee>thamana is a milky beauty</marquee>')

def samantha(request):
    return HttpResponse('<h2>samantha is a beautiful</h2>')