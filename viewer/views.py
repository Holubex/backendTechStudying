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

def hello4(request):

    adjectives = ['great', 'wonderful', 'beautiful']
    context = {'adjectives': adjectives}
    return render(
        request, # predavame na dalsiu stranku request
        template_name="hello.html", # nazov súboru
        context=context # posielame data ako slovnik
    )

def hello5(request, s0):

    s1 = request.GET.get('s1', '')
    return render(
        request, template_name="hello.html",
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )