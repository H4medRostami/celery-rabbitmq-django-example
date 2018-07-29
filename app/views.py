from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import sum
# Create your views here.
def delay(request):
    x = sum.delay(5, 5)
    return HttpResponse(x)

def get(request):
    x = sum.delay(5, 5)
    return HttpResponse(x.get())

def ready(request):
    x = sum.delay(5, 5)
    return HttpResponse(x.ready())