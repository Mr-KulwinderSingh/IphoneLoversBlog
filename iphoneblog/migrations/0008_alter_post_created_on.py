# Generated by Django 3.2.22 on 2023-10-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphoneblog', '0007_auto_20231027_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
