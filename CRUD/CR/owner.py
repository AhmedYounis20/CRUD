from django.views.generic import UpdateView,CreateView,ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



class ownerUpdateView(LoginRequiredMixin,UpdateView):



    def get_queryset(self):
        qs=super(ownerUpdateView,self).get_queryset()
        return qs.filter(owner=self.request.user)


class ownerCreateView(LoginRequiredMixin,CreateView):
    
    def form_valid(self,form):
        print('form valid called')
        object = form.save(commit=False)
        object.owner=self.request.user
        object.save()
        return super(ownerCreateView,self).form_valid(form)

