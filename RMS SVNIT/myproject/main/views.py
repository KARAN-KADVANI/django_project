# main/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def dairy(request):
    return render(request, 'dairy.html')