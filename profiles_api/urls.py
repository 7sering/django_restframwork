from django.urls import path
# from .views import *
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), 
]
