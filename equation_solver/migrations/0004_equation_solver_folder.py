# Generated by Django 2.2.1 on 2019-05-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equation_solver', '0003_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation_solver',
            name='folder',
            field=models.IntegerField(default=0),
        ),
    ]
