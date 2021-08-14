from django import forms
from django.forms import fields, widgets
from .models import Pic,Comment
from django.core.files.uploadedfile import InMemoryUploadedFile
class CreateForm(forms.ModelForm):


    max_upload_limit=3*1024*1024
    

    picture=forms.FileField(    required=False,label='file to upload <='+ str(max_upload_limit/1024) )
    upload_field_name='picture'
    class Meta:
        model=Pic
        fields=['title','text','picture']
    def clean(self):
        cleaned_data=super().clean()
        pic=cleaned_data.get('picture')
        if pic is None:
            return 
        if len(pic) > self.max_upload_limit:
            self.add_error('picture','file uploaded must be less than 3m bytes ')

    def save(self,commit=True):
        instance=super(CreateForm,self).save(commit=False)
        f=instance.picture
        if isinstance(f,InMemoryUploadedFile):
            bytearr=f.read()
            instance.type=f.content_type
            instance.picture = bytearr
        if commit:
            instance.save()
        return instance

class comment_form(forms.ModelForm):
    class Meta():
        model=Comment
        fields=['text']
