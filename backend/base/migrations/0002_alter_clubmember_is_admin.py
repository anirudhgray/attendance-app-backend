# Generated by Django 4.0.6 on 2022-08-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmember',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
