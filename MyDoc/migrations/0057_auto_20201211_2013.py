# Generated by Django 3.1.3 on 2020-12-11 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0056_auto_20201211_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medrecs',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='MyDoc.doctor'),
        ),
    ]