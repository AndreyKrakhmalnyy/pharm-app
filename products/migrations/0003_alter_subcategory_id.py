# Generated by Django 5.0.2 on 2024-02-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_name_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]