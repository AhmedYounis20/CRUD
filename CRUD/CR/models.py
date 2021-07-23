from django.conf import settings
from django.db import models
from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator,MaxLengthValidator
class article(models.Model):
    title= models.CharField(max_length=200,validators=[MinLengthValidator(5,'please write title with length of characters greater than 5'),MaxLengthValidator(10,"sorry title can't exceed 10 charcters ")])
    text=models.TextField()
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='', default='images.png')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    def get_absolute_url(self):
        return reverse('CR:CR')