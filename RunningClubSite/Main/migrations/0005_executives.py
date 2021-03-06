# Generated by Django 2.2.1 on 2019-09-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Treasurer', 'Treasurer'), ('Secretary', 'Secretary'), ('Web/Social Media', 'Web/Social Media'), ('Advisor', 'Advisor')], default='President', max_length=16)),
                ('about', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField()),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
