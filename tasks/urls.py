""" Tasks URL Configuration """
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('category', views.CategoryView)


urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.CategoryListView.as_view()),
]
