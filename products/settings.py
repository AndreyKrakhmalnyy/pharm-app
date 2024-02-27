from dotenv import load_dotenv 

load_dotenv()

SPECTACULAR_SETTINGS = {
    'TITLE': 'PharmApp API',
    'DESCRIPTION': 'Представляет собой API для получения данных о категории товара, подкатегории товара, инструкции \
        к товару и описание основных характеристик самого продукта. Доступ к данным доступен через JWT токен.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}