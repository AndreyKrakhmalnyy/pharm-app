from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
    # # ROOT API (http://127.0.0.1:3000/)
    path('drf-api/', include('products.urls')),
    # DRF-API login (http://127.0.0.1:3000/drf-auth/login/?next=/api-root/)
    path('drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # SWAGGER-UI (http://127.0.0.1:3000/open-api/schema/swagger-ui/)
    path('open-api/', include('utils.api.urls')),
    # JWT (http://127.0.0.1:3000/Jwt/)
    path('Jwt/', include('utils.jwt_auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

