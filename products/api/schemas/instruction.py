from drf_spectacular.utils import extend_schema


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