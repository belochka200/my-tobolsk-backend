from typing import Type

from django.db.models.manager import BaseManager
from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Route
from .serializers import RouteSerializer


class RoutesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset: BaseManager[Route] = Route.objects.all()
    serializer_class: Type[serializers.Serializer] = RouteSerializer
