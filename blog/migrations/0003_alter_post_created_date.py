# Generated by Django 3.2.5 on 2021-08-19 10:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 10, 39, 18, 988641, tzinfo=utc)),
        ),
    ]
