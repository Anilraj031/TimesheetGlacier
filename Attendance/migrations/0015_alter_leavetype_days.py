# Generated by Django 4.1.4 on 2023-02-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0014_alter_leavetype_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavetype',
            name='days',
            field=models.IntegerField(default=3, null=True),
        ),
    ]
