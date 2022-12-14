# Generated by Django 4.1.3 on 2022-12-01 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_publicacion_articulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app1.employe')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('supervisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.empleado')),
            ],
        ),
    ]
