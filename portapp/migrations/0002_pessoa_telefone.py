# Generated by Django 4.1.7 on 2023-10-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default=None, max_length=18),
        ),
    ]
