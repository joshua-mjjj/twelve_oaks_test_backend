from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Global Bites API",
        default_version="v1",
        description="Global Bites Backend",
        contact=openapi.Contact(email="shredakajoshua@gmail.com"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), # Who can view the api 
)

urlpatterns = [
    re_path(
        r"^(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),  # <-- Here
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),  # <-- Here
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/", include("api.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# API Key 
# 0qwHlGVcgxcSTPe5elFi157kMWAbadUI--yDFdT7dyHACVN-NunNuIxEK_hTWYqoZZb8JTShx9fiwP7OP5m1mUR9Wow53gZeDhwMbP1LBqNqUpbwBb6cDENJCL0VZHYx

# Client ID
# oIOjOI9INsNhJW1AuolLzw

