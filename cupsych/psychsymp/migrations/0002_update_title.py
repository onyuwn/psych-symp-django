# Generated by Django 3.2.18 on 2023-03-04 04:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('psychsymp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
