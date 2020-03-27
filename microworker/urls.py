""" microworker URL Configuration """
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework import routers


router = routers.DefaultRouter()
# router.register('url', viewset= )





urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path('', include('micro_profile.urls')),
    path('', include('tasks.urls')),

    path('token-auth/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)