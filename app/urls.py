from django.contrib import admin
from django.urls import path, include
from core.views import home
from core import views
from core.views import lee_sin_view
from core.views import gnar_view
from core.views import warwick_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("vocabulaire/", views.vocabulaire, name="vocabulaire"),
    path("lee_sin/", lee_sin_view, name="lee_sin"),
    path("gnar/", gnar_view, name="gnar"),
    path("warwick/", warwick_view, name="warwick"),
]
