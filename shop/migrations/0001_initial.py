# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 21:25
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('material', models.TextField(blank=True)),
                ('avgSoldPrice', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('lowestCurrListing', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('highestCurrListing', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('lowestSoldLising', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('highestSoldListing', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('lastActive', models.DateTimeField()),
                ('available', models.BooleanField(default=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item', to='shop.Category')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ('-lastActive',),
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditionRating', models.FloatField(default=5.0, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(1.0)])),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=10, validators=[django.core.validators.MinValueValidator(1.0)])),
                ('size', models.CharField(blank=True, max_length=5, null=True)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Lisiting', to='shop.Item')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Listings',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='SubCatergory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='subCatergory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.SubCatergory'),
        ),
        migrations.AlterIndexTogether(
            name='listing',
            index_together=set([('id',)]),
        ),
        migrations.AlterIndexTogether(
            name='item',
            index_together=set([('id', 'slug')]),
        ),
    ]
