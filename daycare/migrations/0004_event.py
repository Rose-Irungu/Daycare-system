# Generated by Django 5.1.3 on 2024-12-05 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycare', '0003_approvedenrollment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]