# Generated by Django 2.2.1 on 2019-09-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20190917_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='executives',
            name='portrait',
            field=models.BooleanField(default=False),
        ),
    ]
