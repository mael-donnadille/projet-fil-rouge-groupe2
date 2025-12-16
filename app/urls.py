from django.contrib import admin
from django.urls import path
from core.views import home
<<<<<<< Updated upstream
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("vocabulaire/", views.vocabulaire, name="vocabulaire"),
]
=======

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
]
>>>>>>> Stashed changes
