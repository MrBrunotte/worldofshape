# Generated by Django 3.0.4 on 2020-05-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_name_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
