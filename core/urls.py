# DJANGO settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    # ROOT API (http://127.0.0.1:3000/)
    path('', include('products.urls')),
    # DRF-API login (http://127.0.0.1:3000/drf-auth/login/?next=/api-root/)
    path('drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # SWAGGER-UI (http://127.0.0.1:3000/open-api/schema/swagger-ui/)
    path('open-api/', include('products.api.urls')),
    # JWT (http://127.0.0.1:3000/v1/jwt/token/)
    path('v1/jwt/', include('products.jwt.urls')),
    # DEBUG TOOLBAR
    path('__debug__/', include('debug_toolbar.urls')),
]



