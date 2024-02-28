from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema
from products.models import Product

from utils.jwt_auth.auth import jwt_auth

from products.api.serializers.product import ProductSerializer

import redis
from utils.cache import settings
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0) 


@extend_schema(tags=['Product'])
class ProductApiView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
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
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Получение конкретного товара со всеми характеристиками по его ID.", 
        description="Для получения необходимо указать ID аптечного товара."
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