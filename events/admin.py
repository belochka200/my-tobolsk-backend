from django.contrib import admin

from .models import Event
from MyTobolsk.utils import get_fields


@admin.register(Event)
class PostAdmin(admin.ModelAdmin):
    fields: list[str] = get_fields(model=Event)
    list_display: list[str] = get_fields(model=Event)
    list_editable: list[str] = get_fields(
        model=Event,
        ignore_fields=['title', 'describe', 'place']
    )

    # insert all fields
    list_filter: list[str] = get_fields(
        model=Event,
        ignore_fields=[field.name for field in Event._meta.get_fields()]
    )
