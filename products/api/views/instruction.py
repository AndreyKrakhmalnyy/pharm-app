from django.conf import settings
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema
from products.models import Instruction

from utils.jwt_auth.auth import jwt_auth

from products.api.serializers.instruction import InstructionsSerializer

import redis
from utils.cache import settings
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0) 


@extend_schema(tags=['Instruction'])
class InstructionsApiView(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionsSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = (IsAuthenticated,)
    authentication_classes = [jwt_auth]
    
    @extend_schema(
        summary="Получение списка с полным описанием инструкций для каждого товара.", 
        description="Представляет собой список словарей с полями: \
            'id' (уникальный идентификатор инструкции) \
            'product' (уникальный идентификатор товара), \
            'name_product (название товара) \
            'composition' (cостав) \
            'peculiarities' (особенности), \
            'product_packaging' (комплектация), \
            'description' (описание), \
            'indications_for_use' (показания), \
            'contraindications' (противопоказания), \
            'mode_of_application' (способ применения), \
            'storage_conditions' (условия хранения)"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @extend_schema(
        summary="Добавление инструкции к товару.", 
        description="Создаёт инструкцию к товару, ID инструкции генерируется автоматически. Для добавления \
        необходимо указать следующие поля: \
            'product' (уникальный идентификатор товара), \
            'name_product (название товара) \
            'composition' (cостав) \
            'peculiarities' (особенности), \
            'product_packaging' (комплектация), \
            'description' (описание), \
            'indications_for_use' (показания), \
            'contraindications' (противопоказания), \
            'mode_of_application' (способ применения), \
            'storage_conditions' (условия хранения)"
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Получение инструкции товара.", 
        description="Для получения необходимо указать ID инструкции. Ответ будет получен в виде словаря с данными: \
            'id' (уникальный идентификатор инструкции) \
            'product' (уникальный идентификатор товара), \
            'name_product (название товара) \
            'composition' (cостав) \
            'peculiarities' (особенности), \
            'product_packaging' (комплектация), \
            'description' (описание), \
            'indications_for_use' (показания), \
            'contraindications' (противопоказания), \
            'mode_of_application' (способ применения), \
            'storage_conditions' (условия хранения)"
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полное обновление инструкции к товару.", 
        description="Изменяет характеристики товара. Требуется ввод всех приведённых характеристик: \
            'id' (уникальный идентификатор инструкции) \
            'product' (уникальный идентификатор товара), \
            'name_product (название товара) \
            'composition' (cостав) \
            'peculiarities' (особенности), \
            'product_packaging' (комплектация), \
            'description' (описание), \
            'indications_for_use' (показания), \
            'contraindications' (противопоказания), \
            'mode_of_application' (способ применения), \
            'storage_conditions' (условия хранения)"
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частичное обновление инструкции к товару.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик: \
            'id' (уникальный идентификатор инструкции) \
            'product' (уникальный идентификатор товара), \
            'name_product (название товара) \
            'composition' (cостав) \
            'peculiarities' (особенности), \
            'product_packaging' (комплектация), \
            'description' (описание), \
            'indications_for_use' (показания), \
            'contraindications' (противопоказания), \
            'mode_of_application' (способ применения), \
            'storage_conditions' (условия хранения)"
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удаление инструкции к товару.", 
        description="Для удаления необходимо указать ID инструкции."
    )       
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)