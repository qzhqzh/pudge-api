from django.urls import include
from django.conf.urls import url

from django.conf.urls.static import static
from . import settings

from .api_urls import urlpatterns as api_urlpatterns
from .html_urls import urlpatterns as html_urlpatterns

from rest_framework.documentation import include_docs_urls

urlpatterns = api_urlpatterns + html_urlpatterns

urlpatterns += [
    url("docs/", include_docs_urls(title="MY API DOCS")),
]

if settings.dev.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.base.MEDIA_URL, document_root=settings.base.MEDIA_ROOT)

    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Snippets API",
            default_version='v1',
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
                      url(r'^swagger(?P<format>\.json|\.yaml)$',
                          schema_view.without_ui(cache_timeout=0), name='schema-json'),
                      url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
                          name='schema-swagger-ui'),
                      url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
                          name='schema-redoc'),
                  ] + urlpatterns

    # https://www.cnblogs.com/yzxing/p/9409474.html
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
