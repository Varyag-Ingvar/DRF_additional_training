"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from women.views import WomenAPIList, WomenAPIRetrieveUpdate, WomenAPIRetrieveDestroy

# from women.views import WomenViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)  # создаем роутер

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/

    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),    # названия методов берем в документации к DRF
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
# ]


"""Упростим паттерны маршрутов (см.код выше)"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/sessionauth/', include('rest_framework.urls')),    # подключаем авторизацию на основе сессий
    path('api/v1/women/', WomenAPIList.as_view()),           # прописываем путь с методом .as_view() для get и post
    path('api/v1/women/<int:pk>/', WomenAPIRetrieveUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIRetrieveDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),          # конфигурируем url для djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # импортируем re_path из Джанго - http://127.0.0.1:8000/auth/token/login/
]
