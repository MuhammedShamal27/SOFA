# Generated by Django 5.0 on 2024-03-12 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_wallet"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
    ]