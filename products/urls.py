from django.urls import path, include
from api.products.views.product import ProductView
from api.products.views.category import CategoryView
from api.products.views.subcategory import SubCategoryView
from api.products.views.instruction import InstructionsView

urlpatterns = [
    path('categories/', CategoryView, name='categories'),
    path('subcategories/', SubCategoryView, name='subcategories'),
    path('products/', ProductView, name='products'),
    path('instructions/', InstructionsView, name='instructions'),
]



















# from products.api.views.product import ProductApiView
# from products.api.views.category import CategoryApiView
# from products.api.views.subcategory import SubCategoryApiView
# from products.api.views.instruction import InstructionsApiView


# from rest_framework import routers

# router = routers.DefaultRouter() 
# router.register(r'category', CategoryApiView, basename='category')
# router.register(r'subcategory', SubCategoryApiView, basename='subcategory')
# router.register(r'products', ProductApiView, basename='products')
# router.register(r'instructions', InstructionsApiView, basename='instructions')

# urlpatterns = [
#     path('', include(router.urls)),
# ]