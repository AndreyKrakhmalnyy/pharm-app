from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from products.models import Product
from utils.jwt_auth.auth import jwt_auth
from api.products.serializers.product import ProductSerializer


@extend_schema(tags=['Product'])
class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
    @method_decorator(cache_page(60))
    @extend_schema(
        summary="Получение списка всех товаров с их характеристиками.", 
        description="Представляет собой список словарей с полями: \
            'category' (уникальный идентификатор категории), \
            'subcategory (уникальный идентификатор подкатегории)', \
            'name_product' (название товара), \
            'price' (стоимость), \
            'volume' (дозировка), \
            'quantity' (количество), \
            'pharmacological_group' (фармгруппа товара), \
            'manufacturer_country' (страна производитель), \
            'manufacturer_company' (компания производитель), \
            'expiration_date' (срок годности), \
            'release_form', (форма выпуска) \
            'access_medicament' (отпуск товара - по рецепту или без рецепта)"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(60))
    @extend_schema(
        summary="Получение конкретного товара со всеми характеристиками по его ID.", 
        description="Для получения необходимо указать ID аптечного товара."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Добавление товара.", 
        description="Создаёт товар по его основным характеристикам, ID товара генерируется автоматически. Для добавления необходимо указать следующие поля: \
            'category' (уникальный идентификатор категории), \
            'subcategory (уникальный идентификатор подкатегории)', \
            'name_product' (название товара), \
            'price' (стоимость), \
            'volume' (дозировка), \
            'quantity' (количество), \
            'pharmacological_group' (фармгруппа товара), \
            'manufacturer_country' (страна производитель), \
            'manufacturer_company' (компания производитель), \
            'expiration_date' (срок годности), \
            'release_form', (форма выпуска) \
            'access_medicament' (отпуск товара - по рецепту или без рецепта)"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полное обновление товара.", 
        description="Изменяет характеристики товара. Требуется ввод всех приведённых характеристик: \
            'id' (ID товара), \
            'name_product' (название товара), \
            'price' (стоимость), \
            'volume' (дозировка), \
            'quantity' (количество), \
            'pharmacological_group' (фармгруппа товара), \
            'manufacturer_country' (страна производитель), \
            'manufacturer_company' (компания производитель), \
            'expiration_date' (срок годности), \
            'release_form' (форма выпуска), \
            'access_medicament' (отпуск препарата - по рецепту или без рецепта), \
            'category' (ID категории), \
            'subcategory' (ID подкатегории)" 
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление товара.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик: \
            'id' (ID товара), \
            'name_product' (название товара), \
            'price' (стоимость), \
            'volume' (дозировка), \
            'quantity' (количество), \
            'pharmacological_group' (фармгруппа товара), \
            'manufacturer_country' (страна производитель), \
            'manufacturer_company' (компания производитель), \
            'expiration_date' (срок годности), \
            'release_form' (форма выпуска), \
            'access_medicament' (отпуск препарата - по рецепту или без рецепта), \
            'category' (ID категории), \
            'subcategory' (ID подкатегории)" 
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление товара.", 
        description="Для удаления товара необходимо указать его ID."
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

ProductView = cache_page(60)(ProductApiView.as_view(methods))