from django.db.models import Model, CharField, TextField, ImageField


class Route(Model):
    title = CharField(verbose_name='title', max_length=255)
    image = ImageField(verbose_name='image', upload_to='routes')
    describe = TextField(verbose_name='describe')

    def __str__(self):
        return self.title
