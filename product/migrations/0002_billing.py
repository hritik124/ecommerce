# Generated by Django 4.1.7 on 2023-05-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=60)),
                ('pincode', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=40)),
            ],
        ),
    ]