# Generated by Django 4.0.5 on 2022-06-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_image_alter_customer_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='static/images/customer'),
        ),
    ]