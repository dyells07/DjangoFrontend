from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginuser,name="login"),
    path('signup',views.signupuser,name="signup"),
    path('logout',views.logoutuser,name="logout"),
    path('about',views.about,name="about"),
    path('contact',views.contactme,name="contact"),
    path('contact',views.song,name="contact")
    
]
