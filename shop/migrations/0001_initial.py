# Generated by Django 5.0.6 on 2024-05-21 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSizeLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Product size in letters',
                'verbose_name_plural': 'Product sizes in letters',
            },
        ),
        migrations.CreateModel(
            name='ProductSizeNumerical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Product numerical size',
                'verbose_name_plural': 'Product numerical sizes',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_image', to='common.media', verbose_name='Brand image')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='CategoryMen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_image_men', to='common.media', verbose_name='Category image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryWomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_image_women', to='common.media', verbose_name='Category image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductMen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('discounted_price', models.FloatField(default=0, verbose_name='Discounted price')),
                ('description', models.TextField(verbose_name='Description')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_product_men', to='shop.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product_men', to='shop.categorymen', verbose_name='Category')),
                ('colors', models.ManyToManyField(to='common.media', verbose_name='Colors')),
                ('image1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_men', to='common.media', verbose_name='Brand image')),
                ('image2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image2_men', to='common.media', verbose_name='Brand image')),
                ('image3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image3_men', to='common.media', verbose_name='Brand image')),
                ('image4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image4_men', to='common.media', verbose_name='Brand image')),
                ('image5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image5_men', to='common.media', verbose_name='Brand image')),
                ('size_letter', models.ManyToManyField(to='shop.productsizeletter', verbose_name='Size in letters')),
                ('size_num', models.ManyToManyField(to='shop.productsizenumerical', verbose_name='Size in numbers')),
            ],
            options={
                'verbose_name': 'Product for men',
                'verbose_name_plural': 'Products for men',
            },
        ),
        migrations.CreateModel(
            name='ProductWomen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('discounted_price', models.FloatField(default=0, verbose_name='Discounted price')),
                ('description', models.TextField(verbose_name='Description')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_product_women', to='shop.brand', verbose_name='Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_product_women', to='shop.categorywomen', verbose_name='Category')),
                ('colors', models.ManyToManyField(to='common.media', verbose_name='Colors')),
                ('image1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_women', to='common.media', verbose_name='Brand image')),
                ('image2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image2_women', to='common.media', verbose_name='Brand image')),
                ('image3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image3_women', to='common.media', verbose_name='Brand image')),
                ('image4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image4_women', to='common.media', verbose_name='Brand image')),
                ('image5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image5_women', to='common.media', verbose_name='Brand image')),
                ('size_letter', models.ManyToManyField(to='shop.productsizeletter', verbose_name='Size in letters')),
                ('size_num', models.ManyToManyField(to='shop.productsizenumerical', verbose_name='Size in numbers')),
            ],
            options={
                'verbose_name': 'Product for women',
                'verbose_name_plural': 'Products for women',
            },
        ),
    ]