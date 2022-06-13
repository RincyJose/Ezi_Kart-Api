# Generated by Django 4.0.5 on 2022-06-13 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.DecimalField(decimal_places=4, max_digits=10)),
                ('weight_total', models.DecimalField(decimal_places=4, max_digits=10)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=200)),
                ('p_price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('p_quantity', models.IntegerField()),
                ('p_stock', models.IntegerField()),
                ('p_barcode', models.CharField(max_length=200)),
                ('p_weight', models.IntegerField()),
                ('orders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to='api.order')),
            ],
        ),
    ]