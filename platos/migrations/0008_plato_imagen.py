# Generated by Django 5.0 on 2024-01-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0007_subcategoria_activa'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
