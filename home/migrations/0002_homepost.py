# Generated by Django 3.1.4 on 2021-01-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featuredblog', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
    ]