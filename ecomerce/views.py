from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ecomerce.forms import ContactForm, RegisterForm, LoginForm

#create function here

def home_page(request):
    context ={
        'title':'Home',
        
    }
    if request.user.is_authenticated:
        context['primium_content'] = 'Primium Oh yeah ! primium content'
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
    contact_form = ContactForm(request.POST or None)
    context ={
        'title':'Contact',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == 'POST':
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    return render(request, 'contact/contact_page.html', context)

def login_page(request):
    form  = LoginForm(request.POST or None)
    print(request.user.is_authenticated)
    context ={
        'title':'Login',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        row_password = form.cleaned_data.get('password')
        user = authenticate(request, username = username, password = row_password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            #context['form'] = LoginForm()
            print('Redirect Success Page')
            return redirect('/')
        else:
            print('Login Error')
    return render(request, 'auth/login_page.html', context)

User = get_user_model()
def register_page(request):
    form  = RegisterForm(request.POST or None)
    context ={
        'title':'Register',
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        row_password = form.cleaned_data.get('password')
        User.objects.create_user()
    return render(request, 'auth/register_page.html', context)