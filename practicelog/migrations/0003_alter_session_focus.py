# Generated by Django 4.1.7 on 2023-03-01 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicelog', '0002_alter_session_date_alter_session_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='focus',
            field=models.JSONField(blank=True, default=list),
        ),
    ]