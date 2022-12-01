# Generated by Django 4.1.3 on 2022-11-30 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_libros_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progenitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_crea', models.DateTimeField(auto_now_add=True)),
                ('fecha_modifica', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8)),
                ('activo', models.BooleanField(default=True)),
                ('padre', models.CharField(max_length=50)),
                ('madre', models.CharField(max_length=50)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.persona')),
            ],
            options={
                'verbose_name_plural': 'Progenitores',
            },
        ),
    ]
