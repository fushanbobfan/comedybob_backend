# Generated by Django 4.2.3 on 2023-08-08 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0002_delete_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('saved_joke_list', models.TextField(null=True)),
                ('time_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
