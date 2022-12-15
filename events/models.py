from django.db.models import Model, CharField, DateField, TimeField, TextField


class Event(Model):
    title: CharField = CharField(verbose_name='title', max_length=255)
    describe: TextField = TextField(verbose_name='describe')
    date: DateField = DateField(verbose_name='Date')
    time: TimeField = TimeField(verbose_name='Time')
    place: CharField = CharField(verbose_name='Place', max_length=255)

    def __str__(self) -> CharField:
        return self.title
