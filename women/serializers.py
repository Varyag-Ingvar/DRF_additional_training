from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    # авторизованный пользователь будет автоматически связываться с создаваемой/изменяемой записью
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        # fields = ("id", "title", "content", "cat")   # поля, которые будут возвращаться клиенту
        fields = "__all__"  # запись в таком формате вернте все поля прописанные в модели





"""Сложный путь написания сериализаторов (изнанка сериализации)"""
# class WomenSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
