from django.contrib.auth import login
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpRequest, request
from .serializers import IhaSerializerGet, IhaSerializerPost, IhaSerializerUpdate, ModelSerializer, CategorySerializer, \
    BrandSerializer
from .models import Iha, Model, Brand, Category
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework import permissions, viewsets
from django.contrib.auth.decorators import login_required
from rest_framework import views
from . import serializers
from rest_framework.decorators import api_view


def loginPage(request):
    return render(request, 'main/login.html')

@login_required
def getUpdatePage(request, pk):
    iha = Iha.objects.get(id=pk)
    context = {
        "iha": iha
    }
    return render(request, 'main/update_page.html', context=context)


def getAdminPage(request):
    return render(request, 'main/admin_list.html')


def getHomePage(request):
    return render(request, 'main/index.html')


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)


class ModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        print(request.GET.get('brand'))
        if request.GET.get('brand') is not None:
            queryset = Model.objects.filter(brand=request.GET.get('brand'))
            serializer = ModelSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Model.objects.all()
            serializer = ModelSerializer(queryset, many=True)
            return Response(serializer.data)


class IhaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Iha.objects.all()
    serializer_class = IhaSerializerGet
    permission_classes_by_action = {'create': [permissions.IsAuthenticated],
                                    'list': [AllowAny]}

    def list(self, request):
        if request.GET.get('brand') is not None:
            queryset = Iha.objects.filter(brand__name__icontains=request.GET.get('brand'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('category') is not None:
            queryset = Iha.objects.filter(category__name__icontains=request.GET.get('category'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('search') is not None:
            queryset = Iha.objects.filter(Q(brand__name__icontains=request.GET.get('search')) | Q(
                category__name__icontains=request.GET.get('search')) | Q(
                model__name__icontains=request.GET.get('search')) | Q(weight__icontains=request.GET.get('search')))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Iha.objects.all()
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = IhaSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def update(self, request, pk, *args, **kwargs):
        instance = Iha.objects.get(pk=pk)
        serializer = IhaSerializerUpdate(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if User.objects.filter(email=email).exists():
            print("email var")
            response_data = {
                "email": "Email already exists"
            }
            return HttpResponse(response_data, status=409)
        elif User.objects.filter(username=username).exists():
            response_data = {
                "username": "Username already exists"
            }
            return HttpResponse(response_data, status=409)
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=lastname, is_active=True)
            user.save()
            return HttpResponse(status=201)
