# Generated by Django 5.1 on 2024-08-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.CharField(max_length=200),
        ),
    ]