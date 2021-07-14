from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import makeForm
from . import models
# Create your views here.
def autos(request):
    return render(request,'autos/autos.html')
def lookup(request):
    return render(request,'autos/lookup.html',{'makes':models.make.objects.all()})

def createMakeView(request):
    if request.method=='GET':
        form=makeForm()
        return render(request,'autos/createmake.html',{'form':form.as_table()})
    else:
        data=makeForm(request.POST)
        if data.is_valid():
            data=models.make(name=request.POST['name'])
            data.save()
            return redirect('/autos/lookup/')
        return redirect(request.path)

def deleteMake(request,id):
    item=models.make.objects.get(id=id)
    item.delete()
    return redirect('/autos/lookup')
def updateMake(request,id):
    if request.method !="POST":

        item=models.make.objects.get(id=id)

        form=makeForm(initial={'name': item.name})
        return render (request,'autos/makeupdate.html',{'form':form})
    else:
        data=request.POST
        print(data)
        if 'name' in data:
            item=models.make.objects.get(id=id)
            item.name=data['name']
            item.save()
        return redirect('/autos/lookup')
        # else:
        #     print(form.is_valid())
        #     return render (request,'autos/makeupdate.html',{'form':form})

def makeView(request):
    form = makeForm()
    return render(request,'make.html',{"form":form})
