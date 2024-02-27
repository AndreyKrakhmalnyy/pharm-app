from drf_spectacular.utils import extend_schema


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