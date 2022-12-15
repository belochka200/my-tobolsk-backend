from django.contrib import admin
from MyTobolsk.utils import get_fields
from .models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    fields: list[str] = get_fields(model=Route)
    list_display: list[str] = get_fields(model=Route)
