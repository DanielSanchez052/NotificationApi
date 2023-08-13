from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Documentación de API",
        default_version='v0.1',
        description="Documentación de API para el manejo de notificaciones",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sanchezd0528@gmail.com"),
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("api/notifications/admin/", admin.site.urls),
    path("api/notifications/", include("apps.notifications.urls")),

    # docs
    re_path(r'^api/notifications/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/notifications/swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/notifications/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc')
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
