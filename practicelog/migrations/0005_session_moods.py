# Generated by Django 4.1.7 on 2023-03-07 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practicelog', '0004_rename_sessions_session_user_alter_session_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='moods',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
