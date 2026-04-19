from django.db import models

# Create your models here.
class  Catagory(models.Model):
    #autoincrement,
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100 ,null=True,blank=True )
    active=models.BooleanField(default=True)