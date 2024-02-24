from drf_spectacular.utils import extend_schema


# Category schema description

def get_categories():
    return extend_schema(
        summary="Получение списка всех категорий товаров.", 
        description="Представляет собой список словарей с полями: \
            'id' (уникальный идентификатор категории), \
            'name_category' (название категории товара)" 
)
    
def post_category():
    return extend_schema(
        summary="Получение категории товара.", 
        description="Для добавления необходимо указать название категории в поле 'name_category' (название категории \
        товара), ID категории товара генерируется автоматически."
    )
    
def get_category_by_id():
    return extend_schema(
        summary="Добавление категории товара.", 
        description="Для получения необходимо указать 'id' категории в поле ввода ниже."
    )
    
def put_category_by_id():
    return extend_schema(
        summary="Полное обновление категории товара.", 
        description="Изменяет характерики категории. Требуется ввод и поля 'id' (уникальный идентификатор категории), \
        и поля 'name_category' (название категории товара).")
             
def patch_category_by_id():
   return extend_schema(
        summary="Частичное обновление категории товара.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик: \
            'id' (уникальный идентификатор категории), \
            'name_subcategory' (название категории)"
    )
    
def delete_category_by_id():
    return extend_schema(
    summary="Удаление категории товара.", 
    description="Для удаления категории товара необходимо указать его ID."
    )

# SubCategory schema description

def get_subcategories():
    return extend_schema(
        summary="Получение списка всех подкатегорий товаров.", 
        description="Представляет собой список словарей с полями: \
            'id' (уникальный идентификатор подкатегории), \
            'name_subcategory' (подкатегория товара), \
            'category' (уникальный идентификатор категории)" 
)
    
def post_subcategory():
    return extend_schema(
        summary="Добавление подкатегории товара.", 
        description="Для добавления необходимо указать название подкатегории в поле 'name_subcategory' \
        и уникальный идентификатор категории товара в поле 'id'."
)
    
def get_subcategory_by_id():
    return extend_schema(
        summary="Получение подкатегории товара по его ID.", 
        description="Для получения необходимо указать ID подкатегории в поле ввода ниже. \
        В ответе также будет получено ID поля 'category' (категория товара)."
    )
    
def put_subcategory_by_id():
    return extend_schema(
        summary="Полное обновление подкатегории товара.", 
        description="Изменяет характерики подкатегории. Требуется ввод всех приведённых характеристик:) \
            'id' (уникальный идентификатор подкатегории), \
            'name_subcategory' (название подкатегории)"
    )
def patch_subcategory_by_id():
   return extend_schema(
        summary="Частичное обновление подкатегории товара.", 
        description="Позволяет изменить только требуемые параметры. Полный список характеристик:) \
            'id' (уникальный идентификатор категории), \
            'name_subcategory' (название категории)"
    )
   
def delete_subcategory_by_id():
    return extend_schema(
    summary="Удаление подкатегории товара.", 
    description="Для удаления подкатегории товара необходимо указать его ID."
    )

# Product schema description

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

# Instruction schema description

def get_instructions():
    return extend_schema(
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
       
def post_instruction():
    return extend_schema(
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
    
def get_instruction_by_id():
    return extend_schema(
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
    
def put_instruction_by_id():
    return extend_schema(
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
    
def patch_instruction_by_id():
    return extend_schema(
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
    
def delete_instruction_by_id():
    return extend_schema(
    summary="Удаление инструкции к товару.", 
    description="Для удаления необходимо указать ID инструкции."
)
    

