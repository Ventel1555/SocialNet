from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})