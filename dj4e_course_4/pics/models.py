from django.db import models
from django.db.models.aggregates import Min
from django.urls import reverse
from django.conf import settings
from django.core.validators import MinLengthValidator
# Create your models here.

class Pic(models.Model):
    title=models.CharField(max_length=250)
    text=models.TextField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    picture=models.BinaryField(null=True,blank=True,editable=True)
    type=models.CharField(max_length=256,null=True,blank=True,help_text='the MIMETYPE of the file ')

    comments= models.ManyToManyField(settings.AUTH_USER_MODEL, through='Comment' , related_name='pic_comments'  )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self,*args,**kwargs):
        return reverse('pics:pic_details',kwargs={'pk': self.pk})
  
class Comment(models.Model):
    text=models.TextField(validators=[MinLengthValidator(3,'please write comment longer than 3 charachters ')])
    pic=models.ForeignKey(Pic,on_delete=models.CASCADE)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    craeted_at =models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text