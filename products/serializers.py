from rest_framework import serializers
from .models import Category, SubCategory, Product, Instruction

class CategorySerializer(serializers.ModelSerializer): # Создаём класс сериализатор для преобразования данных модели в JSON и обратно для взаимодействия с данными через API.
    class Meta:
        model = Category
        fields = '__all__'
        
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class InstructionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'