from django.urls import path
from . import views
urlpatterns=[
    path('',views.autos),
    path('make',views.makeView,name='make')
]