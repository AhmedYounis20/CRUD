from django.urls import path

from . import views 
urlpatterns=[
    path('',views.cats,name='cat'),
    path('lookup/',views.lookup,name='lookup')
]