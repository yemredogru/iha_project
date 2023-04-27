from django.urls import path
from rest_framework import routers
from .views import getHomePage,IhaViewSet,ModelViewSet,BrandViewSet,CategoryViewSet,getAdminPage,getUpdatePage,loginPage,logoutUser,register,addPage,cartPage,cart_add
from django.urls import include

app_name = 'iha_project'
router=routers.DefaultRouter() #Api için yönlendirme tanımlamaları
router.register(r'iha',IhaViewSet,basename='Iha')
router.register(r'model',ModelViewSet,basename='Model')
router.register(r'brand',BrandViewSet,basename='Brand')
router.register(r'category',CategoryViewSet,basename='Category')


urlpatterns = [
    path('list/', getAdminPage, name='news'), #admin ürün listeleme sayfası
    path('add/', addPage, name='add'),#admin ürün ekleme sayfası
    path('login/', loginPage, name='login'),
    path('cart/', cartPage, name='cart'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('add/<product_id>/',cart_add,name='cart_add'),
    path('update/<int:pk>/', getUpdatePage, name='update'), #admin ürün güncelleme sayfası
    path('', getHomePage, name='home'),
    path('api/', include(router.urls)),
]
