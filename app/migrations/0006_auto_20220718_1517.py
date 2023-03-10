# Generated by Django 3.2.5 on 2022-07-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220718_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='uuid',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='degree',
            field=models.CharField(blank=True, choices=[('Phd', 'دکترا'), ('Undergraduate', 'زیر دیپلم'), ('Master', 'فوق لیسانس'), ('Bachelor', 'لیسانس')], max_length=15, null=True, verbose_name='مدرک تحصیلی'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='relation',
            field=models.CharField(choices=[('Partner', 'همسر'), ('Child', 'فرزند')], max_length=7),
        ),
        migrations.AlterField(
            model_name='importantdate',
            name='occasion',
            field=models.CharField(choices=[('anniversary', 'anniversary'), ('birthday', 'birthday')], max_length=11),
        ),
    ]
