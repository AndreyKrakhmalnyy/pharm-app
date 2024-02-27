from django.urls import path, include
from rest_framework import routers
from products.api.views.category import CategoryApiView
from products.api.views.subcategory import SubCategoryApiView
from products.api.views.product import ProductApiView
from products.api.views.instruction import InstructionsApiView

router = routers.DefaultRouter() 
router.register(r'category', CategoryApiView, basename='category')
router.register(r'subcategory', SubCategoryApiView, basename='subcategory')
router.register(r'products', ProductApiView, basename='products')
router.register(r'instructions', InstructionsApiView, basename='instructions')

urlpatterns = [
    path('', include(router.urls)),
]