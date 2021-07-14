from django.shortcuts import render

# Create your views here.
def cats(request):
    return render(request,'cats/cats.html')
def lookup(request):
    return render(request,'cats/lookup.html')