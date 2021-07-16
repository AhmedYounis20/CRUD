from django.db import models

# Create your models here.
class breed(models.Model):
    name=models.CharField(name="name",max_length=100)
    def __str__(self) -> str:
        return self.name
class cat(models.Model):
    nickname=models.CharField(name='nickname',max_length=100)
    weight=models.IntegerField(name="weight")
    foods=models.CharField(name="foods",max_length=100)
    breed=models.ForeignKey(to=breed, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nickname+' ( '+str(self.breed)+' )'