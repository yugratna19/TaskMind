# Generated by Django 5.1.4 on 2025-01-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Not Completed', 'Not Completed'), ('Completed', 'Completed')], default='Not Completed', max_length=20),
        ),
    ]
