from django.urls import path, include
from rest_framework import routers
from products.swagger.views import CategoryApiView, SubCategoryApiView, ProductApiView, InstructionsApiView

router = routers.DefaultRouter() 
router.register(r'category', CategoryApiView, basename='category')
router.register(r'subcategory', SubCategoryApiView, basename='subcategory')
router.register(r'products', ProductApiView, basename='products')
router.register(r'instructions', InstructionsApiView, basename='instructions')

urlpatterns = [
    path('', include(router.urls)), # Подставляем автоматически созданные URL-маршруты от router выше 
]