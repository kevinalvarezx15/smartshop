# Generated by Django 4.0.1 on 2022-07-30 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_alter_compra_compra_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='detalleCompra',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Detalle compra Id'),
        ),
    ]
