from typing import Type
from django.db.models.base import Model

# menu: list[dict[str, str]] = [
#     {
#         'title': 'Главная',
#         'url_name': 'home'
#     },
#     {
#         'title': 'Мероприятия',
#         'url_name': 'events'
#     }
# ]


def get_fields(model: Type[Model], ignore_fields: list['str'] = []) -> list[str]:
    '''
        Возвращает все поля модели, кроме поля id(pk) и полей ignore_fields
        >>> list_display = get_fields(Model, ['field 1', 'field 2'])
    '''
    return [field.name for field in model._meta.get_fields()
            if field.name not in ignore_fields and field.name != 'id']


def get_read_only_fields(model: Type[Model]) -> list[str]:
    '''
        Возвращает поля только для чтения
        >>> readonly_fields = get_read_only_fields(model)
    '''
    return [field.name for field in model._meta.get_fields() if field.editable == False]
