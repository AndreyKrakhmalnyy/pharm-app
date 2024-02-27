from drf_spectacular.utils import extend_schema


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