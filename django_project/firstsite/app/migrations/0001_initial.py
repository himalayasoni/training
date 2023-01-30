# Generated by Django 4.1.5 on 2023-01-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
                ('batting_order', models.CharField(max_length=30)),
            ],
        ),
    ]
