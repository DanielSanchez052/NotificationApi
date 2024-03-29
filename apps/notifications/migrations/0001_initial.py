# Generated by Django 4.1 on 2023-08-17 02:16

import apps.notifications.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('user', models.CharField(blank=True, max_length=36, null=True)),
                ('notification_status', models.CharField(choices=[(None, '(unknown)'), ('PENDING', 'PENDING'), ('CANCELED', 'CANCELED'), ('MANUAL', 'MANUAL'), ('COMPLETE', 'COMPLETED'), ('IN_PROCESS', 'IN PROCESS')], default='PENDING', max_length=20)),
                ('Source', models.CharField(blank=True, max_length=150, null=True)),
                ('config', models.JSONField(verbose_name='config')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notification',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='modified at')),
                ('deleted_at', models.DateField(auto_now=True, verbose_name='deleted at')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('template_path', models.TextField(max_length=255)),
                ('render', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'NotificationTemplate',
                'verbose_name_plural': 'NotificationTemplates',
            },
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, unique=True)),
                ('config', models.JSONField(max_length=500, validators=[apps.notifications.validators.ConfigDefaultValidator], verbose_name='config_default')),
                ('config_schema', models.JSONField(blank=True, max_length=500, null=True, verbose_name='config_schema')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Notification Type',
                'verbose_name_plural': 'Notification Type',
            },
        ),
        migrations.CreateModel(
            name='NotificationResults',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('messages', models.TextField()),
                ('error', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='results', to='notifications.notification')),
            ],
            options={
                'verbose_name': 'Notification Result',
                'verbose_name_plural': 'Notification Results',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='notifications.notificationtemplate'),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notifications.notificationtype'),
        ),
    ]
