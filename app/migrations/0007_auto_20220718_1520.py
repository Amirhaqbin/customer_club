# Generated by Django 3.2.5 on 2022-07-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20220718_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='degree',
            field=models.CharField(blank=True, choices=[('Master', 'فوق لیسانس'), ('Phd', 'دکترا'), ('Bachelor', 'لیسانس'), ('Undergraduate', 'زیر دیپلم')], max_length=15, null=True, verbose_name='مدرک تحصیلی'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]