from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import breedForm,catForm
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def cats(request):
    return render(request,'cats/cats.html',{'cats':models.cat.objects.all(),'breeds':models.breed.objects.all()})
@login_required(login_url='/accounts/login/')

def lookup(request):
    return render(request,'cats/lookup.html',{'breeds':models.breed.objects.all()})

@login_required(login_url='/accounts/login/')
def createBreedView(request):
    if request.method=='GET':
        form=breedForm()
        return render(request,'cats/createbreed.html',{'form':form.as_table()})
    else:
        data=breedForm(request.POST)
        if data.is_valid():
            data=models.breed(name=request.POST['name'])
            data.save()
            return redirect('/cats/')
        return redirect(request.path)

@login_required(login_url='/accounts/login/')
def deleteBreed(request,id):
    if request.method=="GET":
        return render(request,'cats/deletebreed.html',{"breed":models.breed.objects.get(id=id).Name})
    else:
        breed=models.breed.objects.get(id=id)
        breed.delete()
        return redirect('/cats/')

@login_required(login_url='/accounts/login/')
def updateBreed(request,id):
    if request.method =="GET":

        item=models.breed.objects.get(id=id)

        form=breedForm(initial={'name': item.name})
        return render (request,'cats/createbreed.html',{'form':form})
    else:
        data=request.POST
        form = breedForm(data or None )

        if 'name' in data :
            item=models.breed.objects.get(id=id)
            item.name=data['name']
            item.save()
        return redirect('/cats/')
        # else:
        #     print(form.is_valid())
        #     return render (request,'autos/makeupdate.html',{'form':form})


@login_required(login_url='/accounts/login/')
def createCat(request):
    if request.method=='GET':
        form=catForm()

        return render(request,'cats/createcat.html',{'form':form})
    else:
        data=request.POST
        form=catForm(data)
        # form = autoForm(initial={
        # 'Nickname':data['Nickname'],
        # 'Mileage':data['Mileage'],
        # 'Comments':data['Comments'],
        # 'make':models.make.objects.get(id=data['make'])})
        if form.is_valid():
            item=models.cat(
            nickname=data['nickname'],
            weight=data['weight'],
            foods=data['foods'],
            breed=models.breed.objects.get(id=data['breed']))
            item.save()
            return redirect('/cats/')

        return render(request,'cats/createcat.html',{'form':form})

@login_required(login_url='/accounts/login/')
def deleteCat(request,id):
    if request.method=="GET":
        return render(request,'cats/deletecat.html',{"cat":models.cat.objects.get(id=id).nickname})
    else:
        cat=models.cat.objects.get(id=id)
        cat.delete()
        return redirect('/cats/')
@login_required(login_url='/accounts/login/')
def updateCat(request,id):

    if request.method =="GET":

        item=models.cat.objects.get(id=id)

        form=catForm(initial={
            'nickname':item.nickname,
            'weight':item.weight,
            'foods':item.foods,
            'breed':item.breed
        })
        return render (request,'cats/createcat.html',{'form':form})
    else:
        data=request.POST
        form=catForm(data)
        if form.is_valid():
            item=models.cat.objects.get(id=id)
            item.nickname=data['nickname']
            item.weight=data['weight']
            item.foods=data['foods']
            item.breed=models.breed.objects.get(id=data['breed'])
            item.save()
        else:
            return render (request,'cats/createcat.html',{'form':form})

        return redirect('/cats/')