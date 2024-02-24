from django.urls import path
from DiningApp import views

app_name = 'DiningApp'

urlpatterns = [
    path('',views.index, name='index'),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path('category/', views.redirect_to_category_index, name='category'),
]
