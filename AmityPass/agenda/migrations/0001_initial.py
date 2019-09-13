# Generated by Django 2.1.7 on 2019-09-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=70)),
                ('period', models.CharField(blank=True, choices=[('P1', 'Period 1'), ('P2', 'Period 2'), ('P3', 'Period 3'), ('P4', 'Period 4'), ('P5', 'Period 5'), ('P6', 'Period 6'), ('P7', 'Period 7'), ('P8', 'Period 8'), ('ss', 'Spartan Seminar')], default='P1', max_length=2)),
            ],
        ),
    ]