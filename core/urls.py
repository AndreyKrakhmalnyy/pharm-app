from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from products.views import CategoryApiView, SubCategoryApiView, ProductApiView, InstructionsApiView

router = routers.DefaultRouter() # Используется для упрощения процесса создания URL-маршрутов для представлений API
router.register(r'api/cat', CategoryApiView)
router.register(r'api/cat/subcat', SubCategoryApiView)
router.register(r'api/cat/subcat/products', ProductApiView)
router.register(r'api/cat/subcat/products/instructions', InstructionsApiView)

# /api/categories
# /api/categories/<category_id>/subcategories
# /api/subcategories/<subcategory_id>/products
# /api/products/<product_id>/instructions

urlpatterns = [
    path('', include(router.urls)), # Подставляем автоматически созданные URL-маршрутов от router выше 
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]