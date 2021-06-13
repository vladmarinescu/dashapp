from django.urls import path
from . import views
from department_one.dash_apps.apps import main

urlpatterns = [
    path('', views.dashboard, name='department_one')
]