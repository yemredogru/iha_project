from django.urls import path
from rest_framework import routers
from .views import getHomePage,IhaViewSet,ModelViewSet,BrandViewSet,CategoryViewSet,getAdminPage,getUpdatePage,loginPage
from django.urls import include

app_name = 'iha_project'
router=routers.DefaultRouter()
router.register(r'iha',IhaViewSet,basename='Iha')
router.register(r'model',ModelViewSet,basename='Model')
router.register(r'brand',BrandViewSet,basename='Brand')
router.register(r'category',CategoryViewSet,basename='Category')


urlpatterns = [
    path('list/', getAdminPage, name='news'),
    path('login/', loginPage, name='login'),
    path('update/<int:pk>/', getUpdatePage, name='update'),
    path('', getHomePage, name='home'),
    path('api/', include(router.urls)),

]
