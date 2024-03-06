from django.urls import path
from CategoryApp import views

app_name = 'CategoryApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('breakfast/', views.breakfast, name="breakfast"),
    path('lunch/', views.lunch, name="lunch"),
    path('dinner/', views.dinner, name="breakfast"),
    path('dining/', views.redirect_to_dining_index, name="dining"),
    path('form/', views.form, name="form"),

    # path("contact/",views.contact,name="contact"),
    # path("about/",views.about,name="about"),
    # path("category/",views.category,name="category"),
]
