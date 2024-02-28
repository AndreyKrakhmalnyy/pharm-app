from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema
from products.models import Category

from utils.jwt_auth.auth import jwt_auth

from products.api.serializers.category import CategorySerializer

import redis
from utils.cache import settings
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0) 


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
        summary="Добавление категории товара.", 
        description="Для получения необходимо указать 'id' категории в поле ввода ниже."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Получение категории товара.", 
        description="Для добавления необходимо указать название категории \
        в поле 'name_category' (название категории \
        товара), ID категории товара генерируется автоматически."
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