from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('special'):
        characters.extend('~!@#$%^&*')

    if request.GET.get('numbers'):
        characters.extend('123456789')

    length = int(request.GET.get('length',12))
    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')