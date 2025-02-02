# Generated by Django 5.1.1 on 2024-09-16 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_column', models.IntegerField(default=None, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_pivot', to='catalog.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_pivot', to='catalog.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='catalog.ProductCategory', to='catalog.category'),
        ),
    ]
