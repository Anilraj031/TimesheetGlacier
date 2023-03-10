# Generated by Django 4.1.5 on 2023-01-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0002_leavetype_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='leave',
            name='approval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Attendance.approval'),
        ),
    ]
