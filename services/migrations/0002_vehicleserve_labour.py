# Generated by Django 3.1.7 on 2021-05-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleserve',
            name='labour',
            field=models.CharField(default='', max_length=300),
        ),
    ]
