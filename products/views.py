# DJANGO REST FRAMEWORK
# from django.conf import settings
from rest_framework import viewsets
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# OPENAPI/SWAGGER-UI
from drf_spectacular.utils import extend_schema
# products/models.py
from products.models import Category, SubCategory, Instruction, Product
# JWT
from rest_framework_simplejwt.authentication import JWTAuthentication
# products/serializers.py
from products.serializers import (
    CategorySerializer, 
    SubCategorySerializer, 
    ProductSerializer, 
    InstructionsSerializer)
# REDIS
# import json
# import redis

# redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, 
#                                   port=settings.REDIS_PORT, db=0) # Создаём экземпляр Redis соединения, 
#                                     # используя настройки хоста и порта из Django settings


@extend_schema(tags=['Category'])
class CategoryApiView(viewsets.ModelViewSet): 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
    
    # @extend_schema(tags=['Category-cash'])
    # @action(detail=False, methods=['get', 'post'])
    # def manage_items(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         items = {}
    #         count = 0
    #         for key in redis_instance.keys("*"):
    #             items[key.decode("utf-8")] = redis_instance.get(key)
    #             count += 1
    #         response = {
    #             'count': count,
    #             'msg': f"Found {count} items.",
    #             'items': items
    #         }
    #         return Response(response, status=200)

    #     elif request.method == 'POST':
    #         item = json.loads(request.body)
    #         key = list(item.keys())[0]
    #         value = item[key]
            
    #         # Проверяем, есть ли данные с таким ключом в кэше
    #         if redis_instance.exists(key):
    #             cached_value = redis_instance.get(key)
    #             response = {
    #                 'msg': f"Data already exists in cache for key: {key}, value: {cached_value}"
    #             }
    #             return Response(response, status=200)
            
    #         # Сохраняем данные в кэше
    #         redis_instance.set(key, value)
    #         response = {
    #             'msg': f"Data saved in cache for key: {key}, value: {value}"
    #         }
    #         return Response(response, status=201)

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

    
