from django.db import models
from .common.fileUpload.userDirectoryPath import userDirectoryPath
# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Model(models.Model):
    brand=models.ForeignKey(Brand,verbose_name=('Model'),on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name='Model Adı')

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name=models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.name}"

class Iha(models.Model):
    id = models.AutoField(primary_key=True)
    brand=models.ForeignKey(Brand,null=True,blank=True,verbose_name='Marka',on_delete=models.CASCADE)
    model=models.ForeignKey(Model,null=True,blank=True,verbose_name='Model',on_delete=models.CASCADE)
    weight=models.IntegerField(null=True,blank=True,verbose_name='Ağırlık')
    category=models.ForeignKey(Category,verbose_name='Kategori',null=True,blank=True,on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True, verbose_name='Fiyat')
    img=models.ImageField(upload_to=userDirectoryPath,null=True,blank=True,verbose_name=('Iha resmi'))
