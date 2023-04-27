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
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart

from rest_framework import views
from . import serializers

from django.core import serializers as serialize
from rest_framework.decorators import api_view


def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Iha, id=product_id) #id'ye sahip ürün yoksa 404 ekranına git

    cart.add(
            product=product,
            quantity=1,
            update_quantity=True)
    return render(request, 'main/cart.html', context={'cart': cart})

def cartPage(request):
    cart = Cart(request)


    return render(request, 'main/cart.html', context={'cart': cart})
@login_required(login_url='/login/')
def addPage(request):
    return render(request,'main/add_other.html')
@login_required(login_url='/login/')
def logoutUser(request):
    logout(request)
    return redirect('/login/')
def loginPage(request):
    if request.method=="GET":
        return render(request, 'main/login.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            return redirect('/login/')

@login_required(login_url='/login/')
def getUpdatePage(request, pk):
    iha = Iha.objects.get(id=pk)
    context = {
        "iha": iha
    }
    return render(request, 'main/update_page.html', context=context)

@login_required(login_url='/login/')
def getAdminPage(request):
    return render(request, 'main/admin_list.html')

@login_required(login_url='/login/')
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
    #Create işlemi yaparken yetkili kullanıcının işlem yapabilmesini sağlamak için action'a göre yetki kısıtlaması getirdik

    def list(self, request):
        #?query'leri yakalayabilmek için aşağıdaki ifleri oluşturduk
        if request.GET.get('brand') is not None:
            queryset = Iha.objects.filter(brand__name__icontains=request.GET.get('brand')) #örnek olarak ?brand=deneme için deneme değişkenini GET.get('brand') ile aldık ve brand name'i deneme içerenleri filtreledik
            serializer = IhaSerializerGet(queryset, many=True) #serializer'a bu verileri gönderdik
            return Response(serializer.data) #serializer içerisindeki data'yı return ettik, bu veri json olarak return oldu
        elif request.GET.get('category') is not None:
            queryset = Iha.objects.filter(category__name__icontains=request.GET.get('category'))
            serializer = IhaSerializerGet(queryset, many=True)
            return Response(serializer.data)
        elif request.GET.get('search') is not None:
            queryset = Iha.objects.filter(Q(brand__name__icontains=request.GET.get('search')) | Q(
                category__name__icontains=request.GET.get('search')) | Q(
                model__name__icontains=request.GET.get('search')) | Q(weight__icontains=request.GET.get('search'))) # Q() sorgu'su complex sorgular için kullanılır, birden fazla sorgu olduğu için Q kullandım
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
        serializer = IhaSerializerUpdate(instance, data=request.data, partial=True) #sadece değişen alanların güncellenmesi için partial=True verdik

        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = request.POST['username'] #body içerisinde username'i aldık
        password = request.POST['password']


        if User.objects.filter(username=username).exists(): #username veritabanında kayıtlı mı diye kontrol ettik
            response_data = {
                "username": "Kullanıcı adı zaten kayıtlı"
            }
            return render(request,'main/register.html',context=response_data)
        else:
            user = User.objects.create_user(username=username, password=password, is_active=True)
            user.save()
            response_data = {
                "success": "Kullanıcı oluşturma başarılı"
            } #success'i htmlde ekrana bastırabilmek için tanımladık
            return render(request, 'main/register.html', context=response_data)
    else:
        return render(request,'main/register.html')