# Generated by Django 3.2.5 on 2022-07-18 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerClub', '0008_alter_gift_allowed_to_used_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='allowed_to_used_duration',
            field=models.IntegerField(choices=[(365, 'year'), (7, 'week'), (1, 'day'), (30, 'month')], verbose_name='مدت اعتبار'),
        ),
    ]
