# Generated by Django 4.1.6 on 2023-02-13 06:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_userprofile_username_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='api_key',
            field=models.UUIDField(default=uuid.UUID('96eeb830-656a-486e-9132-1d313c015684'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('ffcabbb0-ab6a-11ed-b531-e9b49344f47a'), primary_key=True, serialize=False),
        ),
    ]