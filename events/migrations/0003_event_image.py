# Generated by Django 4.1.4 on 2022-12-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_describe'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='', upload_to='events', verbose_name='image'),
            preserve_default=False,
        ),
    ]
