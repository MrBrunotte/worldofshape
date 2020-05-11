# Generated by Django 3.0.4 on 2020-05-11 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200511_1103'),
        ('checkout', '0003_auto_20200511_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('program', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductLineItem',
        ),
    ]
