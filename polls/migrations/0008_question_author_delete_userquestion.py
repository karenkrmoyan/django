# Generated by Django 5.1.4 on 2024-12-17 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_alter_question_pub_date_alter_userquestion_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.polluser'),
        ),
        migrations.DeleteModel(
            name='UserQuestion',
        ),
    ]