# Generated by Django 4.1.5 on 2023-02-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app2", "0002_remove_order_place"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="paid_amount",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
