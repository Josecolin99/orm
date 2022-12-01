# Generated by Django 4.1.3 on 2022-12-01 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_progenitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.padre')),
            ],
        ),
    ]
