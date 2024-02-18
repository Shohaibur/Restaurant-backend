from django.contrib import admin
from django.urls import path
from dining import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/',views.categories,name="categories"),
    path('categories/breakfast/',views.breakfast,name="breakfast"),
    path('categories/lunch/',views.lunch,name="lunch"),
    path('categories/dinner/',views.dinner,name="dinner"),
    path('home',views.home,name="home"),
    path('home/categories/',views.categories,name="categories"),
    path('',views.home,name="home"),

]
