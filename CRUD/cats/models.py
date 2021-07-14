from django.db import models

# Create your models here.
class breed(models.Model):
    name=models.CharField(name="Name",max_length=100)
    def __str__(self) -> str:
        return self.Name
class cat(models.Model):
    nickname=models.CharField(name='Nickname',max_length=100)
    weight=models.IntegerField(name="Weight")
    foods=models.CharField(name="foods",max_length=100)
    breed=models.ForeignKey(to=breed, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Nickname+' ( '+str(self.breed)+' )'