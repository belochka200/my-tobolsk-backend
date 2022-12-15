from django.db.models import (
    Model,
    CharField,
    TextField,
    DateField,
    TimeField,
    ImageField
)


class Story(Model):
    title = CharField(verbose_name='title', max_length=255)
    image = ImageField(verbose_name='image', upload_to='stories')
    describe = TextField(verbose_name='describe')
    date = DateField(verbose_name='Date', auto_now_add=True)
    time = TimeField(verbose_name='Time', auto_now_add=True)

    def __str__(self) -> str:
        return self.title
