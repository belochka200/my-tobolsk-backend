# Generated by Django 4.1.4 on 2022-12-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='describe',
            field=models.TextField(verbose_name='describe'),
        ),
    ]
