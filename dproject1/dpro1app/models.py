from django.db import models

# Create your models here.
class  travel(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
class meetteam(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
