# Generated by Django 4.1.4 on 2022-12-11 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_alter_story_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]