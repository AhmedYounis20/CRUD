from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
APP_NAME = 'ChucksList'

urlpatterns = [
    path('', views.HomeView.as_view()),
]
