# Generated by Django 4.0.5 on 2022-06-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=200)),
                ('address', models.CharField(default='', max_length=300)),
                ('age', models.IntegerField(default=0, max_length=123)),
            ],
        ),
    ]