# Generated by Django 2.2.1 on 2019-05-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equation_solver', '0004_equation_solver_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='equation_solver',
            name='name',
            field=models.TextField(default='No name'),
        ),
    ]
