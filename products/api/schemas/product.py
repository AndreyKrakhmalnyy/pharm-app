from drf_spectacular.utils import extend_schema


def get_products():
    return extend_schema(
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
    

    
def post_product():
    return extend_schema(
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
    
def get_product_by_id():
    return extend_schema(
        summary="Получение конкретного товара со всеми характеристиками по его ID.", 
        description="Для получения необходимо указать ID аптечного товара."
    )
    
def put_product_by_id():
    return extend_schema(
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
    
def patch_product_by_id():
    return extend_schema(
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
    
def delete_product_by_id():
    return extend_schema(
    summary="Удаление товара.", 
    description="Для удаления товара необходимо указать его ID."
    )
