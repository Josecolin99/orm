# Generated by Django 4.1.3 on 2022-11-29 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_libros'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='libros',
            unique_together={('nombre', 'tipo')},
        ),
    ]