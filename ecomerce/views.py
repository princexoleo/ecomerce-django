from django.http import HttpResponse
from django.shortcuts import render

#create function here

def home_page(request):
    context ={
        'title':'Home',
    }
    return render(request, 'home/home_page.html', context)

