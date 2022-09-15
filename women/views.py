from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics, viewsets
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
#     """мы можем переопределять метод get_queryset для реализации более сложного поведения при отборе записей из БД"""
#
#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#
#         if not pk:     # если в маршрут не передан id записи, то вернем список из первых трех записей
#             return Women.objects.all()[:3]  # queryset всегда должен возвращать список!(можем отобразить первые три записи)
#
#         return Women.objects.filter(pk=pk)  # если в url передан id, т.е. например ...women/5/, то вернем список из одной конкретной записи
#
#
#     """с помощью декоратора @action мы создаем новый url - http://127.0.0.1:8000/api/v1/women/category
#     и можем задавать уникальное поведение функции представления по этому маршруту"""
#
#     @action(methods=['get'], detail=False)  # detail=False означает, что будут выводится все записи из БД методом get
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [cat.name for cat in cats]}) # получаем список всех категорий из БД
#
#
# """Мы можем красиво управлять доступными конкретному классу методами, добавляя или убирая миксины из
# модуля viewsets, т.е. удаляя из списка аргументов соответсвующий миксин мы, например, отключаем возможность
# удалять или изменять записи в БД"""
# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer



"""Этот код тоже можно упростить с помощью viewsets (см. код выше)"""

class WomenAPIList(generics.ListCreateAPIView):
    """Класс на базе generics.ListCreateAPIView позволяет реализовать 'get' и 'post' методы из-под капота DRF"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ) # неавторизованный юзер может только просматривать записи


class WomenAPIRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Класс на базе generics.UpdateAPIView позволяет реализовать 'put' и 'patch' методы из-под капота DRF"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )  # только юзер, который создал запись, может ее изменять


class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
    """Класс на базе generics.DestroyAPIView позволяет реализовать 'delete' метод из-под капота DRF"""
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )  # только админ может удалять запись, а просматривать любой


# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """Класс на базе generics.RetrieveUpdateDestroyAPIView позволяет реализовать
#     'get', 'put','patch', 'delete' методы для отдельных записей из-под капота DRF"""
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer





"""сложный путь создания вьюх на базе класса APIView, можно упростить, (см. код выше)"""
# class WomenAPIView(APIView):
    # def get(self, request):
    #     queryset = Women.objects.all()
    #     return Response({'posts': WomenSerializer(queryset, many=True).data})
    #
    # def post(self, request):
    #     serializer = WomenSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT not allowed"})
    #
    #     try:
    #         instance = Women.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Object does not exists"})
    #
    #     serializer = WomenSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})




