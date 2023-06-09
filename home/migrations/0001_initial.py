# Generated by Django 3.1.7 on 2021-04-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]