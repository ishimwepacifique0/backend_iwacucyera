# Generated by Django 4.1.2 on 2022-10-20 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwacu', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diy',
            name='description',
            field=models.TextField(),
        ),
    ]
