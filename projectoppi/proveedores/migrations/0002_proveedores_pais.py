# Generated by Django 4.0.1 on 2022-02-18 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0007_tipodocumento_pais'),
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedores',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.paises'),
        ),
    ]