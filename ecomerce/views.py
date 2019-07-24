from django.http import HttpResponse
from django.shortcuts import render

#create function here

def home_page(request):
    context ={
        'title':'Home',
    }
    return render(request, 'home/home_page.html', context)

#about pages
def about_page(request):
    context ={
        'title':'About',
    }
    return render(request, 'about/about_page.html', context)
#
# contact pages
def contact_page(request):
    context ={
        'title':'Contact',
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('name'))
    return render(request, 'contact/contact_page.html', context)