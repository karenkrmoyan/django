# Generated by Django 5.1.4 on 2024-12-16 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_userquestion_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 16, 12, 39, 44, 417746, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 16, 12, 39, 44, 418687, tzinfo=datetime.timezone.utc)),
        ),
    ]
