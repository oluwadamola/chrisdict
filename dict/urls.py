
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search),
    path('word', views.search, name='word'),
]
