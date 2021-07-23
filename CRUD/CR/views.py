from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .owner import ownerCreateView,ownerUpdateView
# Create your views here.

class articleCreateView(ownerCreateView):
    
    model=models.article
    fields=('title','text')
    template_name="cr/create_form.html"
class articleUpdateView(ownerUpdateView):
    model=models.article
    fields=('title','text')
    template_name="cr/create_form.html"
class articleListView(LoginRequiredMixin,ListView):
    
    model=models.article
    template_name='cr/article_list.html'
class articleDetailView(LoginRequiredMixin,DetailView):
    model=models.article
    template_name='cr/detail.html'







