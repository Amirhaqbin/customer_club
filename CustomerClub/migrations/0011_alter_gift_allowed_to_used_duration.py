# Generated by Django 3.2.5 on 2022-07-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerClub', '0010_alter_gift_allowed_to_used_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='allowed_to_used_duration',
            field=models.IntegerField(choices=[(7, 'week'), (1, 'day'), (365, 'year'), (30, 'month')], verbose_name='مدت اعتبار'),
        ),
    ]
