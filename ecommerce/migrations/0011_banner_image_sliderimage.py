# Generated by Django 5.1.4 on 2025-01-19 04:08

import ecommerce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_product_a_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerAbout', models.ImageField(blank=True, null=True, upload_to=ecommerce.models.getFileName)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=ecommerce.models.getFileName_new)),
            ],
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ManyToManyField(blank=True, related_name='slider_images', to='ecommerce.image')),
            ],
        ),
    ]
