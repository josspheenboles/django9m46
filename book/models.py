from django.db import models
from catagory.models import *
# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    name =models.CharField(max_length=100)
    description=models.TextField()
    version=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    publish_date=models.DateField(blank=True,null=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    # onetoone=models.OneToOneField(Catagoty,on_delete=models.CASCADE)
    # manytmany=models.ManyToManyField(Catagory)






