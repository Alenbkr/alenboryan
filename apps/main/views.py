# apps/main/views.py
from django.shortcuts import render

def main(request):
    return render(request, 'main/main.html')  # убедись, что main

