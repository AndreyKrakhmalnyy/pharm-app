from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema
from products.models import SubCategory

from utils.jwt_auth.auth import jwt_auth

from api.products.serializers.subcategory import SubCategorySerializer

    
@extend_schema(tags=['SubCategory'])
class SubCategoryApiView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
    @method_decorator(cache_page(60))
    @extend_schema(
        summary="Получение списка всех подкатегорий товаров.", 
        description="Представляет собой список словарей с полями: \
            'id' (уникальный идентификатор подкатегории), \
            'name_subcategory' (подкатегория товара), \
            'category' (уникальный идентификатор категории)" 
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60))
    @extend_schema(
        summary="Получение подкатегории товара по его ID.", 
        description="Для получения необходимо указать ID подкатегории в поле ввода ниже. \
        В ответе также будет получено ID поля 'category' (категория товара)."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Добавление подкатегории товара.", 
        description="Для добавления необходимо указать название подкатегории \
        в поле 'name_subcategory' и уникальный идентификатор категории товара в поле 'id'."
    )       
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полное обновление подкатегории товара.", 
        description="Изменяет характерики подкатегории. Требуется ввод всех приведённых характеристик:) \
            'id' (уникальный идентификатор подкатегории), \
            'name_subcategory' (название подкатегории)"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление подкатегории товара.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик:) \
            'id' (уникальный идентификатор категории), \
            'name_subcategory' (название категории)"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление подкатегории товара.", 
        description="Для удаления подкатегории товара необходимо указать его ID."
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

SubCategoryView = cache_page(60)(SubCategoryApiView.as_view(methods))