# Generated by Django 3.1.3 on 2020-12-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0042_recept'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='height',
            field=models.IntegerField(default=130),
        ),
        migrations.AddField(
            model_name='patient',
            name='weight',
            field=models.IntegerField(default=65),
        ),
    ]
