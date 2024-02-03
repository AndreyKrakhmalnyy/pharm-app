from django.shortcuts import render
from rest_framework import viewsets
from products.models import Category, SubCategory, Instruction, Product
from products.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer, InstructionsSerializer


class CategoryApiView(viewsets.ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    
class SubCategoryApiView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get']
     
class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class InstructionsApiView(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsSerializer
    http_method_names = ['get']
    
