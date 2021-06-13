from django.urls import path
from . import views
from home.dash_apps.apps import main

urlpatterns = [
    path('', views.home, name='home')
]