# Generated by Django 3.2.2 on 2021-05-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameboard', '0002_auto_20210515_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='content',
            field=models.TextField(),
        ),
    ]