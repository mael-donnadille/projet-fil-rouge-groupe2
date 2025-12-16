from django.contrib import admin
from django.urls import path
from core.views import home
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vocabulaire/", views.vocabulaire, name="vocabulaire"),
]