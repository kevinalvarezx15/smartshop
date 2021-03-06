# Generated by Django 4.0.1 on 2022-02-18 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0007_tipodocumento_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False, verbose_name='Número documento')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('correo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo electrónico')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección')),
                ('dateCreate', models.DateTimeField(auto_now=True, null=True)),
                ('dateUpdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('departamentoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.departamentos')),
                ('municipioId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.municipios')),
                ('tipoDocumentoId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cliente.tipodocumento', verbose_name='Tipo documento')),
            ],
            options={
                'db_table': 'tblProveedores',
            },
        ),
    ]
