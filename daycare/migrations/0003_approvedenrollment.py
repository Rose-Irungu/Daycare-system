# Generated by Django 5.1.3 on 2024-12-05 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0002_rename_parent_email_enrollment_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_date', models.DateTimeField(auto_now_add=True)),
                ('enrollment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='approved_enrollment', to='daycare.enrollment')),
            ],
        ),
    ]
