# Generated by Django 4.1.3 on 2023-01-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=32)),
                ('population', models.CharField(max_length=32)),
            ],
        ),
    ]
