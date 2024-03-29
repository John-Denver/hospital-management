# Generated by Django 3.1.3 on 2020-12-13 19:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0065_auto_20201213_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Format YYYY/MM/DD'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_check',
            field=models.DateField(blank=True, default='2002/03/13', help_text='Format YYYY/MM/DD'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_check',
            field=models.DateField(blank=True, default='2002/03/13', help_text='Format YYYY/MM/DD'),
        ),
    ]
