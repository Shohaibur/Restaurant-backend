from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from CategoryApp.models import Category, Item
from CategoryApp import forms

# Create your views here.


# def index (request):
#   return HttpResponse("List of Category <br> <a href='breakfast/''>Breakfast</a> <br> <a href='lunch/''>Lunch</a> <br> <a href='dinner/''>Dinner</a> <br> <a href='dining/''>Home</a> ")
# def breakfast(request):
#   return HttpResponse ("Welcome to Breakfast <br> <a href='/CategoryApp''>Back</a> ")
# def lunch(request):
#   return HttpResponse ("Welcome to Lunch <br> <a href='/CategoryApp''>Back</a> ")
# def dinner(request):
#   return HttpResponse ("Welcome to Dinner <br> <a href='/CategoryApp''>Back</a> ")
# def redirect_to_dining_index(request):
#   return redirect('DiningApp:index')

def index(request):
    category_list = Category.objects.order_by('name')
    diction = {'categories': category_list}
    return render(request, 'CategoryApp/index.html', context=diction)


def breakfast(request):
    diction = {}
    return render(request, 'CategoryApp/breakfast.html', context=diction)


def lunch(request):
    diction = {}
    return render(request, 'CategoryApp/lunch.html', context=diction)


def dinner(request):
    diction = {}
    return render(request, 'CategoryApp/dinner.html', context=diction)


def redirect_to_dining_index(request):
    return redirect('DiningApp:index')


def form(request):
    new_form = forms.reservation_form()
    diction = {'test_form': new_form}
    if request.method == 'POST':
        new_form = forms.reservation_form(request.POST)

        if new_form.is_valid():
            user_name = new_form.cleaned_data["user_name"]
            user_email = new_form.cleaned_data['user_email']
            reservation_time = new_form.cleaned_data['reservation_time']
            reservation_date = new_form.cleaned_data['reservation_date']

            diction.update({'user_name': user_name})
            diction.update({'user_email': user_email})
            diction.update({'reservation_date': reservation_date})
            diction.update({'reservation_time': reservation_time})
            diction.update({'form_submitted': "Yes"})  # Note: This line updates the value to "Yes"

    return render(request, 'CategoryApp/form.html', context=diction)


