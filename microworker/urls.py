""" microworker URL Configuration """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MicroWorker API",
        default_version='v1'
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
# router.register('url', viewset= )



urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include(router.urls)),

    path('', include('micro_profile.urls')),
    path('', include('tasks.urls')),
    path('', include('chat.urls')),


    path('docs-swag/', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    path('docs-yasg/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),

    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
