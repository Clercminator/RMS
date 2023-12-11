from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.staticfiles import finders
from django.template.loader import get_template
from django.views import View
import os, io, reportlab
from xhtml2pdf import pisa


from .models import *
from .forms import *
from .decorators import *

# Create your views here.

def home(request):

    condominio = Condominio.objects.all()

    return render(request, 'condominios/home.html', {'condominio':condominio})


#__________________________Dashboad - Página inicial para los vecinos.__________________________

@login_required(login_url='login') #people must be logged in to access this page. Otherwise, it'll be redirected to the login page.
@allowed_users(allowed_roles=['authenticated'])
def dashboard(request):
    condominio = request.user.condominio
    print(condominio)
    return render(request, 'condominios/dashboard.html', {'condominio':condominio})



#__________________________Autenticación__________________________

@unauthenticated_user
def registerPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.danger(request, 'Ya este usuario existe, intenta iniciar sesión.')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            
            group = Group.objects.get(name='authenticated')
            user.groups.add(group)
            Condominio.objects.create(user=user, name=user.username)
            
            messages.success(request, 'Tu cuenta ha sido creada existosamente ' + username)
            return redirect('login')
        
    context = {}
    return render(request, 'condominios/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión!')
            return redirect('dashboard')
        else:
            messages.info(request, 'Hubo un error! Verifica que el usuario y/o la contraseña son correctos.')
            return redirect('login')

    context = {}
    return render(request, 'condominios/login.html', context)

def logoutUser(request):

    logout(request)
    return redirect('home')



#__________________________Autenticación__________________________