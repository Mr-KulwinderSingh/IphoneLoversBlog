# Generated by Django 3.2.22 on 2023-10-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphoneblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]