from django.shortcuts import render
from django.http import HttpResponse
import random



def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ""
    lenght = int(request.GET.get('lenght',12))
    characters = list('abcdefghijklmopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@£$%^&*()_+'))

    

    

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password':thepassword})

def contact(request):
    return HttpResponse('<h1>hello its me contact page </h1>')

def about(request):
    return render(request, 'generator/about.html')





# Create your views here.
