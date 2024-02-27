from rest_framework import serializers
from products.models import Instruction

class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'