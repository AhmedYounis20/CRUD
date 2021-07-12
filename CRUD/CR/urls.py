from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 

urlpatterns=[

path('',views.main,name='index'),
path('accounts/login/',views.loginView,name='login'),
path('accounts/logout/',views.logoutView,name='logout'),




]