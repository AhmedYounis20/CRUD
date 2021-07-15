from django.db import models

# Create youhelpr models here.
class make(models.Model):
        
    name=models.CharField(name="name",max_length=100)
    def __str__(self) -> str:
        return self.name


        
class auto(models.Model):
    nickname=models.CharField(name="nickname",max_length=100)
    mileage=models.IntegerField(name="mileage")
    comments=models.CharField(name="comments",max_length=100)
    make=models.ForeignKey(to=make,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nickname+' ( '+str(self.make)+' )'