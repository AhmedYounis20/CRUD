from django.shortcuts import render,redirect
from  django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import makeForm,autoForm
from . import models
# Create your views here.
@login_required(login_url='/accounts/login/')
def autos(request):
    return render(request,'autos/autos.html',{'autos':models.auto.objects.all(),'makes':models.make.objects.all()})

@login_required(login_url='/accounts/login/')
def lookup(request):
    return render(request,'autos/lookup.html',{'makes':models.make.objects.all()})

@login_required(login_url='/accounts/login/')
def createMakeView(request):
    if request.method=='GET':
        form=makeForm()
        return render(request,'autos/createmake.html',{'form':form.as_table()})
    else:
        data=makeForm(request.POST)
        if data.is_valid():
            data=models.make(name=request.POST['name'])
            data.save()
            return redirect('/autos/')
        return redirect(request.path)

@login_required(login_url='/accounts/login/')
def deleteMake(request,id):
    if request.method=="GET":
        return render(request,'autos/deletemake.html',{"make":models.make.objects.get(id=id).name})
    else:
        make=models.make.objects.get(id=id)
        make.delete()
        return redirect('/autos/')

@login_required(login_url='/accounts/login/')
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
        return redirect('/autos/')
        # else:
        #     print(form.is_valid())
        #     return render (request,'autos/makeupdate.html',{'form':form})


@login_required(login_url='/accounts/login/')
def createAuto(request):
    if request.method=='GET':
        form=autoForm()

        return render(request,'autos/createauto.html',{'form':form})
    else:
        data=request.POST
        form=autoForm(data)
        # form = autoForm(initial={
        # 'Nickname':data['Nickname'],
        # 'Mileage':data['Mileage'],
        # 'Comments':data['Comments'],
        # 'make':models.make.objects.get(id=data['make'])})
        print(form.errors)
        if form.is_valid():
            item=models.auto(
            nickname=data['nickname'],
            mileage=data['mileage'],
            comments=data['comments'],
            make=models.make.objects.get(id=data['make']))
            item.save()
            return redirect('/autos/')
        else :
            return HttpResponse(str(form.errors))
            # return render(request,'autos/createauto.html',{'form':form})

@login_required(login_url='/accounts/login/')
def deleteAuto(request,id):
    if request.method=="GET":
        return render(request,'autos/deleteAuto.html',{"Auto":models.auto.objects.get(id=id).nickname})
    else:
        auto=models.auto.objects.get(id=id)
        auto.delete()
        return redirect('/autos/')

@login_required(login_url='/accounts/login/')
def updateAuto(request,id):

    if request.method =="GET":

        item=models.auto.objects.get(id=id)

        form=autoForm(initial={
            'nickname':item.nickname,
            'mileage':item.mileage,
            'comments':item.comments,
            'make':item.make
        })
        return render (request,'autos/autoupdate.html',{'form':form})
    else:
        data=request.POST
        form=autoForm(data)
        if form.is_valid():
            item=models.auto.objects.get(id=id)
            item.nickname=data['nickname']
            item.mileage=data['mileage']
            item.comments=data['comments']
            item.make=models.make.objects.get(id=data['make'])
            item.save()
        else:
            return render (request,'autos/autoupdate.html',{'form':form})

        return redirect('/autos/')