# Generated by Django 2.2.2 on 2019-06-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Cooking', 'Кулинария'), ('Auto', 'Авто'), ('Home', 'Дом'), ('Children', 'Дети'), ('Another', 'Другое')], max_length=250),
        ),
    ]
