from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import redirect
from CategoryApp import forms


def index(request):
    diction = {"text_1": "Using Dictionary"}
    return render(request, 'DiningApp/index.html', context=diction)


def contact(request):
    diction = {}
    return render(request, 'DiningApp/contact.html', context=diction)


def about(request):
    diction = {}
    return render(request, 'DiningApp/about.html', context=diction)


def redirect_to_category_index(request):
    return redirect('CategoryApp:index')




