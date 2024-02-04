# DRF
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Swagger
from drf_spectacular.utils import extend_schema
# models
from products.models import Category, SubCategory, Instruction, Product
# JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
# serializers
from products.serializers import (
    CategorySerializer, 
    SubCategorySerializer, 
    ProductSerializer, 
    InstructionsSerializer)

@extend_schema(tags=['Category'])
class CategoryApiView(viewsets.ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

@extend_schema(tags=['SubCategory'])
class SubCategoryApiView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

@extend_schema(tags=['Product'])
class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

@extend_schema(tags=['Instruction'])
class InstructionsApiView(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]

    
