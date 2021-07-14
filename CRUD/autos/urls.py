from django.urls import path
from . import views
urlpatterns=[
    path('',views.autos),
    path('make',views.makeView,name='make'),
    path('lookup/',views.lookup,name='lookup'),
    path('lookup/create/',views.createMakeView,name='createMake'),
    path('lookup/<int:id>/delete',views.deleteMake,name='deleteMake'),
    path('lookup/<int:id>/update',views.updateMake,name='updateMake'),

]