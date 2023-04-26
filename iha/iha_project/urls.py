from django.urls import path
from rest_framework import routers
from .views import getHomePage,IhaViewSet,ModelViewSet,BrandViewSet,CategoryViewSet,getAdminPage,getUpdatePage
from django.urls import include

app_name = 'iha_project'
router=routers.DefaultRouter()
router.register(r'iha',IhaViewSet,basename='Iha')
router.register(r'model',ModelViewSet,basename='Model')
router.register(r'brand',BrandViewSet,basename='Brand')
router.register(r'category',CategoryViewSet,basename='Category')


urlpatterns = [
    path('list/', getAdminPage, name='news'),
    path('update/<int:pk>/', getUpdatePage, name='news'),
    path('', getHomePage, name='news'),
    path('api/', include(router.urls)),

]
