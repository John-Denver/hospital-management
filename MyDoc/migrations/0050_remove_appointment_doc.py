# Generated by Django 3.1.3 on 2020-12-10 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0049_auto_20201210_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='doc',
        ),
    ]
