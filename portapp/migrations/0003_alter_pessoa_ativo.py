# Generated by Django 4.1.7 on 2023-10-21 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0002_pessoa_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
