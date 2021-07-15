from django.urls import path
from . import views
urlpatterns=[
    path('',views.autos),
    path('lookup/',views.lookup,name='lookup'),
    path('lookup/create/',views.createMakeView,name='createMake'),
    path('lookup/<int:id>/delete',views.deleteMake,name='deleteMake'),
    path('lookup/<int:id>/update',views.updateMake,name='updateMake'),
    path('main/create/',views.createAuto,name="autoCreate"),
    path('main/<int:id>/delete/',views.deleteAuto,name='deleteAuto'),
    path('main/<int:id>/update/',views.updateAuto,name='updateAuto'),


]