import json
from django.core.cache import cache
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema
from products.models import Instruction

from utils.jwt_auth.auth import jwt_auth

from products.api.serializers.instruction import InstructionsSerializer
from products.api.schemas.instruction import (
    get_instructions, post_instruction, get_instruction_by_id,
    put_instruction_by_id, patch_instruction_by_id, delete_instruction_by_id,
)

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
    
    @get_instructions()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @post_instruction()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_instruction_by_id()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @put_instruction_by_id()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @patch_instruction_by_id()
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @delete_instruction_by_id()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)