from rest_framework import viewsets
from products.models import Category
from utils.jwt_auth.auth import jwt_auth
from drf_spectacular.utils import extend_schema
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from api.products.serializers.category import CategorySerializer


# def preload_cache():
#     categories = Category.objects.all()
#     return categories

# preload_cache()

@extend_schema(tags=['Category'])
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
      
        
    @extend_schema(
        summary="Получение списка всех категорий товаров.", 
        description="Представляет собой список словарей с полями: \
             'id' (уникальный идентификатор категории), \
             'name_category' (название категории товара)",
    ) 
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(
        summary="Получение категории товара.", 
        description="Для добавления необходимо указать название категории \
        в поле 'name_category' (название категории \
        товара), ID категории товара генерируется автоматически."
    )   
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Добавление категории товара.", 
        description="Для получения необходимо указать 'id' категории в поле ввода ниже."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полное обновление категории товара.", 
        description="Изменяет характерики категории. Требуется ввод и поля 'id' (уникальный идентификатор категории), \
        и поля 'name_category' (название категории товара)."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление категории товара.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик: \
            'id' (уникальный идентификатор категории), \
            'name_subcategory' (название категории)"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление категории товара.", 
        description="Для удаления категории товара необходимо указать его ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


methods = {
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'post': 'create',
    'delete': 'destroy'
}

CategoryView = cache_page(60)(CategoryApiView.as_view(methods))

















    # def list(self, request, *args, **kwargs):
    #     cached_categories = cache.get('categories_objects')
        
    #     if cached_categories is None:
    #         cached_categories = CategorySerializer(self.queryset, many=True)  
    #         cache.set('categories_objects', cached_categories)
    #     return Response(cached_categories)