# Generated by Django 2.2.1 on 2019-09-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_auto_20190917_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executives',
            name='picture',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
