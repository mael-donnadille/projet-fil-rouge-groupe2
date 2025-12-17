from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("roles/", views.roles, name="roles"),
    path("carte/", views.carte_page, name="carte"),
    path("conseils/", views.conseils_page, name="conseils"),


    path("vocabulaire/", views.vocabulaire, name="vocabulaire"),
    path("choix_perso/", views.choix_perso_view, name="choix_perso"),

    path("lee_sin/", views.lee_sin_view, name="lee_sin"),
    path("gnar/", views.gnar_view, name="gnar"),
    path("warwick/", views.warwick_view, name="warwick"),
]
