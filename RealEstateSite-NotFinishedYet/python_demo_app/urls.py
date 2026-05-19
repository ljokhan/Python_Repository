from django.urls import path
from . import views

urlpatterns = [
    path('python_demo_app/', views.python_demo_app, name ='python_demo_app'),
]