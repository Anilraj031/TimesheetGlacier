# Generated by Django 4.1.4 on 2023-01-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='lbreak',
        ),
        migrations.AddField(
            model_name='attendance',
            name='day',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lbreak1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='lbreak2',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
