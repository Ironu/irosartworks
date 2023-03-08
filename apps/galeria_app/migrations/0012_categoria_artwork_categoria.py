# Generated by Django 4.1.3 on 2023-03-03 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galeria_app', '0011_rename_created_date_artwork_fecha_de_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='nombre')),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='galeria_app.categoria'),
        ),
    ]
