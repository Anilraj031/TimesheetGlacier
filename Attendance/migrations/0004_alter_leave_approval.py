# Generated by Django 4.1.5 on 2023-01-10 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0003_approval_alter_leave_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='approval',
            field=models.ForeignKey(default='Pending', null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.approval'),
        ),
    ]
