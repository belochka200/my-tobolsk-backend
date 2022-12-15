from django.db.models import Model, CharField, TextField


class Route(Model):
    title: CharField = CharField(verbose_name='title', max_length=255)
    describe: TextField = TextField(verbose_name='describe')

    def __str__(self) -> str:
        return self.title
