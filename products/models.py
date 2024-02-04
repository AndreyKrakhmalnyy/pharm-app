from django.db import models


class Category(models.Model): # Описывает тип аптечного товара (лекарства, БАДы и витамины, косметика и т.д.)
    name_category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_category
    
class SubCategory(models.Model): # Описывает классификацию типа товарв (например, БАДы и витамины --> БАДы для мужчин, БАДы для улучшения памяти и т.д.)
    name_subcategory = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Одна категория имеет несколько подкатегорий, т.е. 'ForeignKey' (one-to-many)
    
    def __str__(self):
        return self.name_subcategory
    
class Product(models.Model): # Описывает основные характеристики выбранного товара
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE) # Одна подкатегория имеет несколько продуктов, т.е. 'ForeignKey' (one-to-many) 
    name_product = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=10) # Стоимость
    volume = models.CharField(max_length=10, null=True, blank=True) # Объём
    quantity = models.IntegerField(null=True, blank=True) # Количество
    pharmacological_group = models.CharField(max_length=50, null=True, blank=True) # Фарм. группа препарата 
    manufacturer_country = models.CharField(max_length=30) # Страна производитель
    manufacturer_company = models.CharField(max_length=30) # Компания производитель
    expiration_date = models.CharField(max_length=50, null=True, blank=True) # Срок годности
    release_form = models.CharField(max_length=100, null=True, blank=True) # Форма выпуска (таблетки или сироп)
    access_medicament = models.CharField(max_length=12, null=True, blank=True) # Отпуск препарата (по рецепту или без рецепта)
    
    def __str__(self):
        return self.name_product
    
class Instruction(models.Model): # Инструкции к применению
    product = models.OneToOneField(Product, on_delete=models.CASCADE) # Один продукт имеет одну инструкцию, т.е. 'OneToOneField' (one-to-one)
    name_product = models.CharField(max_length=100, null=True, blank=True)
    composition = models.TextField(max_length=2000, null=True, blank=True) # Состав
    peculiarities = models.TextField(max_length=2000, null=True, blank=True) # Особенности
    product_packaging = models.TextField(max_length=2000, null=True, blank=True) # Комплектация
    description = models.TextField(max_length=2000) # Описание
    indications_for_use = models.TextField(max_length=2000, null=True, blank=True) # Показания
    contraindications = models.TextField(max_length=2000, null=True, blank=True) # Противопоказания
    mode_of_application = models.TextField(max_length=2000, null=True, blank=True) # Способ применения
    storage_conditions = models.TextField(max_length=2000, null=True, blank=True) # Условия хранения

    def __str__(self):
        return self.name_product