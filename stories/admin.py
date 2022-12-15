from django.contrib import admin

from MyTobolsk.utils import get_fields, get_read_only_fields

from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields: list[str] = get_fields(Story)
    list_display: list[str] = get_fields(Story)
    readonly_fields: list[str] = get_read_only_fields(Story)
