# Generated by Django 4.2.20 on 2025-04-20 18:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_socialmediaurls_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('reset_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_used', models.BooleanField(default=False)),
                ('expires_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'core_password_reset',
            },
        ),
    ]
