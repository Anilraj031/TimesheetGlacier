# Generated by Django 4.1.5 on 2023-01-10 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0004_alter_leave_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='leave_from',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='leave',
            name='leave_to',
            field=models.DateField(null=True),
        ),
    ]
