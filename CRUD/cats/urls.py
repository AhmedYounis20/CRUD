from django.urls import path
from . import views
urlpatterns=[
    path('',views.cats,name='cats'),
    path('lookup/',views.lookup,name='lookup'),
    path('lookup/create/',views.createBreedView,name='createBreed'),
    path('lookup/<int:id>/delete',views.deleteBreed,name='deleteBreed'),
    path('lookup/<int:id>/update',views.updateBreed,name='updateBreed'),
    path('main/create/',views.createCat,name="createCat"),
    path('main/<int:id>/delete/',views.deleteCat,name='deleteCat'),
    path('main/<int:id>/update/',views.updateCat,name='updateCat'),
    path('try', views.catListView.as_view()),
    path('try2/<int:pk>', views.catUpdateView.as_view())


]