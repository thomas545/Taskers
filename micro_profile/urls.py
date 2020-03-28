""" Profile URL Configuration """
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('url', viewset= )


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
]
