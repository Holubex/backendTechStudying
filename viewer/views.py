from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# view definovana pomococu funkcie
def hello(request):
    return HttpResponse("Hello World!")

def hello2(request, s):
    return HttpResponse(f'Hello {s} world!')


#URL encoding
def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} world!')