from django.db.models.manager import BaseManager
# from django.shortcuts import HttpResponse, render
from rest_framework import serializers, viewsets

# from MyTobolsk.utils import menu

from .models import Event
from .serializers import EventSerializer


# def main(request) -> HttpResponse:
#     data: dict[str, Union[str, list]] = {
#         'title': 'Главная',
#         'menu': menu
#     }
#     return render(request, 'events/main.html', data)


# def events(request) -> HttpResponse:
#     data: dict[str, Union[str, list]] = {
#         'title': 'Мероприятия',
#         'menu': menu
#     }
#     return render(request, 'events/events.html', data)


class EventsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
