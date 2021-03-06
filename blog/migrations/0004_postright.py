# Generated by Django 3.1.4 on 2021-01-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postright',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=155)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
