import validate
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from CategoryApp.models import Category, Item
from CategoryApp import forms


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
        diction.update({'test_form': new_form})

        if new_form.is_valid():
            user_name = new_form.cleaned_data["user_name"]
            user_email = new_form.cleaned_data['user_email']
            user_phone_num = new_form.cleaned_data['user_phone_num']
            reservation_time = new_form.cleaned_data['reservation_time']
            reservation_date = new_form.cleaned_data['reservation_date']
            guest_no = new_form.cleaned_data['guest_no']
            special_req = new_form.cleaned_data['special_req']

            diction.update({'form_submitted': "Yes"})
            diction.update({'guest_no': guest_no})
            diction.update({'special_req': special_req})
            diction.update({'user_name': user_name})
            diction.update({'user_email': user_email})
            diction.update({'user_phone_num': user_phone_num})
            diction.update({'reservation_date': reservation_date})
            diction.update({'reservation_time': reservation_time})

    return render(request, 'CategoryApp/form.html', context=diction)
