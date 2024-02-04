from django.contrib import admin
from django.urls import path, include
from authorization import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from products.views import CategoryApiView, SubCategoryApiView, ProductApiView, InstructionsApiView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

router = routers.DefaultRouter() # Используется для упрощения процесса создания URL-маршрутов для представлений API
router.register(r'api/category', CategoryApiView, basename='category')
router.register(r'api/subcategory', SubCategoryApiView, basename='subcategory')
router.register(r'api/products', ProductApiView, basename='products')
router.register(r'api/instructions', InstructionsApiView, basename='instructions')

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    #______________API_______________#
    path('', include(router.urls)), # Подставляем автоматически созданные URL-маршруты от router выше 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #______________Swagger_______________#
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #______________JWT_______________#
    path('JWT/api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('JWT/api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('JWT/api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]