from django.shortcuts import render
from django.http import HttpResponse
from .forms import makeForm
# Create your views here.
def autos(request):
    return render(request,'autos/autos.html')
def makeView(request):
    form = makeForm()
    return render(request,'make.html',{"form":form})