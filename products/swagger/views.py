# DJANGO REST FRAMEWORK
import json
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# REDIS
import redis
CACHE_TTL = 3600
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0) 

# OPENAPI/SWAGGER-UI
from drf_spectacular.utils import extend_schema
from .models import Category, SubCategory, Instruction, Product

# jwt-auth/auth.py
from products.jwt.auth import jwt_auth
   
# products/api/serializers.py
from .serializers import (
    CategorySerializer, SubCategorySerializer, 
    ProductSerializer, InstructionsSerializer
)

# products/api/schema.py
from .schema import (
    #Category schema description
    get_categories, post_category, get_category_by_id,
    put_category_by_id, patch_category_by_id, delete_category_by_id,

    # SubCategory schema description
    get_subcategories, post_subcategory,get_subcategory_by_id, 
    put_subcategory_by_id, patch_subcategory_by_id, delete_subcategory_by_id,
    
    # Product schema description
    get_products, post_product, get_product_by_id, 
    put_product_by_id, patch_product_by_id, delete_product_by_id,

    # Instruction schema description
    get_instructions, post_instruction, get_instruction_by_id, 
    put_instruction_by_id, patch_instruction_by_id, delete_instruction_by_id
)
    
                                
# Category API
@extend_schema(tags=['Category'])
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
    @action(detail=False, methods=['get'])
    def get_cache(self):
        if redis_client.exists('category'):
            cached_categories = json.loads(redis_client.get('category'))
            return Response(cached_categories, status=status.HTTP_200_OK)
        else:
            any_categories = [category.to_json() for category in self.queryset]
            redis_client.set('category', json.dumps(any_categories), ex=CACHE_TTL)
            return Response(any_categories, status=status.HTTP_200_OK)
        
    @get_categories()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @post_category()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_category_by_id()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @put_category_by_id()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @patch_category_by_id()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_category_by_id()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
# SubCategory API    
@extend_schema(tags=['SubCategory'])
class SubCategoryApiView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
        
    @get_subcategories()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @get_subcategory_by_id()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @post_subcategory()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @put_subcategory_by_id()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @patch_subcategory_by_id()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_subcategory_by_id()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
# Product API
@extend_schema(tags=['Product'])
class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
    @get_products()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @post_product()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @get_product_by_id()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @put_product_by_id()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @patch_product_by_id()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_product_by_id()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# Instruction API
@extend_schema(tags=['Instruction'])
class InstructionsApiView(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]

    @get_instructions()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @post_instruction()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @get_instruction_by_id()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @put_instruction_by_id()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @patch_instruction_by_id()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_instruction_by_id()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)




    


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
    
    # @staticmethod
    # def get_all_categories():
    #     categories = Category.objects.all()
    #     return [category.to_json() for category in categories]

    # @api_view(['GET'])
    # def list(self, request):
    #     if redis_client.exists('category'):
    #         cached_categories = redis_client.get('category')
    #         return Response(cached_categories, status=status.HTTP_200_OK)
    #     else:
    #         any_categories = self.get_all_categories()
    #         redis_client.set('category', any_categories, ex=CACHE_TTL)
    #         return Response(any_categories, status=status.HTTP_200_OK)   
    
    
