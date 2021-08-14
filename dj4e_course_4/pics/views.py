from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.utils.translation import templatize
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms,models
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
class CreatePic(LoginRequiredMixin ,CreateView):
    template_name='pic_form.html'
    form_class =forms.CreateForm
    def form_valid(self,form):
        object=form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return super(CreatePic,self).form_valid(form)


class PicDetails(DeleteView):
    def get_context_data(self, **kwargs):
        ctx=super().get_context_data(**kwargs)

        comments=models.Comment.objects.filter(pic=ctx['pic'])
        ctx['comments']=comments
        ctx['comment_form']=forms.comment_form()
        return ctx
    template_name='pic_details.html'
    model=models.Pic



class UpdatePic(UpdateView):
    template_name='pic_form.html'
    model=models.Pic

    form_class=forms.CreateForm

class PicListView(LoginRequiredMixin,ListView):
    template_name='pic_list.html'
    model=models.Pic

class DeletePic(LoginRequiredMixin,DeleteView):
    template_name='delete_pic.html'
    model=models.Pic
    def get_queryset(self) :
        return super(DeletePic,self).get_queryset().filter(owner=self.request.user)
    success_url='/pics'

def file_stream(request,pk):
    pic=get_object_or_404(models.Pic,pk=pk)
    response= HttpResponse()
    response['content-type']=pic.type
    response['content-length']=len(pic.picture)
    response.write(pic.picture)
    return response


class CreateCommentView(LoginRequiredMixin ,View):
    def post(self,request,pk):
        pic=get_object_or_404(models.Pic,pk=pk)
        comment=models.Comment(text=request.POST['text'],owner=self.request.user,pic=pic)
        comment.save()
        return redirect(reverse('pics:pic_details',args=[pk]))

    
class DeleteCmmentView(LoginRequiredMixin,View):
    def get(self,request,pk1,pk2):
        if request.user == models.Comment.objects.get(pk=pk2).owner :
            return render(request,'delete_comment.html',{'comment':models.Comment.objects.get(pk=pk2)})
        else :
            return redirect(reverse('pics:pic_details',args=[pk1]))
    def post(self,request,pk1,pk2):
        comment=models.Comment.objects.get(pk=pk2)
        comment.delete()
        return redirect(reverse('pics:pic_details',args=[pk1]))
    model=models.Comment
    pic=models.Comment.pic
