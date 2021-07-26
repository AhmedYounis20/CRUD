from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from .owner import OwnerCreateView,OwnerDeleteView,OwnerListView,OwnerDetailView,OwnerUpdateView
# Create your views here.
def index(request):
    return render(request,'base_menu.html')

class AdCreateView(OwnerCreateView):
     model=models.Ad
     fields=('title','price','text')
     template_name='ad_form.html'

class AdUpdateView(OwnerUpdateView):
     model=models.Ad
     fields=('title','price','text')
     template_name='ad_form.html'
     
    
class AdListView(OwnerListView):
    model=models.Ad
    template_name='ad_list.html'
class AdDeleteView(OwnerDeleteView):
    model=models.Ad
    template_name='delete_ad.html'
    success_url='/ads'
class AdDetailView(OwnerDetailView):
    model=models.Ad
    template_name='ad_detail.html'