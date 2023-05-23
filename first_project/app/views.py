from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
import datetime 
from os import listdir

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    dt = datetime.datetime.now()
    current_time = dt.strftime('%Hчасов|%Mминут  /  %m.%d.%Y года')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    pathway = '/workdir/'
    answer =[]
    if request.path ==  pathway:
        for i in listdir('.'):
            answer = answer + [i, ', ']
        return HttpResponse(answer)  
    raise NotImplemented
