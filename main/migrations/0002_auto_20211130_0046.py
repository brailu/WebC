# Generated by Django 2.2.12 on 2021-11-30 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='name'),
        ),
    ]
