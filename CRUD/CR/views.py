from django.shortcuts import render,redirect
from django. http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import loginForm
# Create your views here.

def main(request):
    return render(request,'main.html')
def loginView(request):
    if request.method=="POST":
    
        data=request.POST
        form = loginForm(data)

        if form.is_valid():
            username=data['username']
            password=data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                print(data['next'])
                return redirect(data['next'])
            
        
        return render(request,'login.html',{'error':True,'form':form})
    else :
        form=loginForm()
        print(form.as_table())
        return render(request,'login.html',{'next':request.GET['next'] ,'error':False,'form':form})

def logoutView(request):
    logout(request)
    return redirect('/')



