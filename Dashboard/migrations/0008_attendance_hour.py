# Generated by Django 4.1.4 on 2023-01-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_alter_attendance_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='hour',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
