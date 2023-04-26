from rest_framework import serializers
from .models import Brand,Model,Iha,Category
from django.contrib.auth import authenticate




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=('name','id',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.brand_name = validated_data.get('brand_name', instance.title)
        instance.save()
        return instance

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Model
        fields=('brand','name','id',)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.model_brand = validated_data.get('model_brand', instance.model_brand)
        instance.model_name = validated_data.get('model_name', instance.model_name)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name','id',)

class IhaSerializerPost(serializers.ModelSerializer):

    class Meta:
        model=Iha
        fields=('brand','model','weight','category','img','id','price')

class IhaSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model=Iha
        fields=('brand','model','weight','category','img','id','price')
class IhaSerializerGet(serializers.ModelSerializer):
    brand=BrandSerializer()
    model=ModelSerializer()
    category=CategorySerializer()
    class Meta:
        model=Iha
        fields=('brand','model','weight','category','img','id','price')

