# Generated by Django 3.0.4 on 2020-05-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20200512_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
