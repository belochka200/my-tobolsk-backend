from django.db.models import Model, CharField, DateField, TimeField, TextField, ImageField


class Event(Model):
    title = CharField(verbose_name='title', max_length=255)
    image = ImageField(verbose_name='image', upload_to='events')
    describe = TextField(verbose_name='describe')
    date = DateField(verbose_name='Date')
    time = TimeField(verbose_name='Time')
    place = CharField(verbose_name='Place', max_length=255)

    def __str__(self):
        return self.title
