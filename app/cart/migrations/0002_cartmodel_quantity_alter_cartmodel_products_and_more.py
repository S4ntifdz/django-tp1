# Generated by Django 4.2.4 on 2023-08-21 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_rename_quantity_stock_product_quantity_stock'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartmodel',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cartmodel',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock_product'),
        ),
        migrations.DeleteModel(
            name='product_with_qt',
        ),
    ]
