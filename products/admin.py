from django.contrib import admin
from .api.models import Category, SubCategory, Product, Instruction

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Instruction)
