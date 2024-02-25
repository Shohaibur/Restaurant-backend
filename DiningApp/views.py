from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import redirect



# Create your views here.

# def index(request):
#   return HttpResponse("Welcome to Restaurant <br> <a href='/DiningApp/category/''> Category </a> <br> <a href='/DiningApp/contact/''>contact </a> <br> <a href='about/''>about </a>")
# def contact(request):
#   return HttpResponse("Contact Page <br> <a href='/DiningApp''>Home </a> <br> <a href='/DiningApp/about/''>about </a> ")
# def about(request):
#   return HttpResponse("About Page <br> <a href='/DiningApp''>Home </a> <br> <a href='/DiningApp/contact/''>contact </a> ")
# def redirect_to_category_index(request):
#   return redirect('CategoryApp:index')

def index(request):
  diction = { "text_1" : "Using Dictionary" }
  return render(request, 'DiningApp/index.html', context=diction)
def contact(request):
  diction = {}
  return render(request,'DiningApp/contact.html',context=diction)
def about(request):
  diction = {}
  return render(request,'DiningApp/about.html',context=diction)
def redirect_to_category_index(request):
  return redirect('CategoryApp:index')
