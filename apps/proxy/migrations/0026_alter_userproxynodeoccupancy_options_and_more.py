# Generated by Django 4.2.6 on 2024-01-23 02:45

from decimal import Decimal

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("proxy", "0025_alter_occupancyconfig_color"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userproxynodeoccupancy",
            options={"verbose_name": "用户占用记录", "verbose_name_plural": "用户占用记录"},
        ),
        migrations.AddField(
            model_name="relaynode",
            name="enlarge_scale",
            field=models.DecimalField(
                decimal_places=1,
                default=Decimal("1.0"),
                max_digits=10,
                verbose_name="倍率",
            ),
        ),
    ]
