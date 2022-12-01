from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import *
from profiles_api import views

#? View Set URLs Router 
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

#?Modal View Set no need to call base_name
router.register('profile', views.UserProfileViewSet)

# ? Regular Urls
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
