"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('CR.urls'),),
    path('autos/',include('autos.urls')),
    path('',views.main,name='index'),
    path('accounts/login/',views.loginView,name='login'),
    path('accounts/logout/',views.logoutView,name='logout'),
    path('cr/',include(('CR.urls','CR'),namespace="CR")),
    path('avatar/',include('avatar.urls')),
    path('cats/',include(('cats.urls','cats'),namespace='cats')),
    path('home/', include('home.urls')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

