from django.contrib import admin
# Register your models here.
from .models import Iha,Model,Category,Brand

@admin.register(Iha)
class IhaAdmin(admin.ModelAdmin):
    list_display=('brand','model','weight','category')

    class Meta:
        model=Iha

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display=('name','brand')

    class Meta:
        model=Model

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)

    class Meta:
        model=Category

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)

    class Meta:
        model=Brand