# Generated by Django 3.1 on 2020-08-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('password', models.IntegerField()),
                ('address1', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]
