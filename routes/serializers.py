from rest_framework import serializers
from .models import Route
from typing import Type


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[Route] = Route
        fields: list[str] = [field.name for field in Route._meta.get_fields()]
