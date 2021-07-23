from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views 

urlpatterns=[
path('',views.articleListView.as_view(),name='CR'),

path('create',views.articleCreateView.as_view(),name='index'),
path('update/<int:pk>',views.articleUpdateView.as_view(),name='index'),

path('detail/<int:pk>',views.articleDetailView.as_view(),name='index'),




]