# Generated by Django 3.1.6 on 2021-03-04 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arucikk',
            name='db',
            field=models.IntegerField(),
        ),
    ]