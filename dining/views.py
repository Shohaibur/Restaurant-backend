from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (response):
  return HttpResponse("Restaurant App <br> <p><a href=categories/>List of categories</p> <br> ")
def breakfast (response):
  return HttpResponse("Welcome to breakfast <p><a href=../>Back</p> ")
def lunch (response):
  return HttpResponse("Welcome to lunch <p><a href=../>Back</p>")
def dinner (response):
  return HttpResponse("Welcome to dinner <p><a href=../>Back</p>")
def categories (response):
  return HttpResponse("List of categories <br>  <p> <a href=breakfast/>Breakfast </p> <p> <a href=lunch/>Lunch </p> <a href=dinner/>Dinner <p><a href=../>Home</p> ")