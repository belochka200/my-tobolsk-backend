from rest_framework import serializers
from .models import Story
from typing import Union


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields: Union[str, list[str]] = "__all__"
        # fields: list[str] = [field.name for field in Story._meta.get_fields()]
