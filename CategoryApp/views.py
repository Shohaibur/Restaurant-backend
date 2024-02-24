from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.


def index (request):
  return HttpResponse("List of Category <br> <a href='breakfast/''>Breakfast</a> <br> <a href='lunch/''>Lunch</a> <br> <a href='dinner/''>Dinner</a> <br> <a href='dining/''>Home</a> ")
def breakfast(request):
  return HttpResponse ("Welcome to Breakfast <br> <a href='/CategoryApp''>Back</a> ")
def lunch(request):
  return HttpResponse ("Welcome to Lunch <br> <a href='/CategoryApp''>Back</a> ")
def dinner(request):
  return HttpResponse ("Welcome to Dinner <br> <a href='/CategoryApp''>Back</a> ")
def redirect_to_dining_index(request):
  return redirect('DiningApp:index')