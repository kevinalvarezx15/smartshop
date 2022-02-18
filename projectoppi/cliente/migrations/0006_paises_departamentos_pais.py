# Generated by Django 4.0.1 on 2022-02-18 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_clientes_celular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'db_table': 'tblPaises',
            },
        ),
        migrations.AddField(
            model_name='departamentos',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.paises', verbose_name='Paises'),
        ),
    ]
