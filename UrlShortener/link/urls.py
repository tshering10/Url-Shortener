from django import urls
from django.urls import path
from .views import home, return_to_orginal

urlpatterns = [
 path('', home, name="home"),   
 path('<str:short_url>/', return_to_orginal, name="redirect"),
]
