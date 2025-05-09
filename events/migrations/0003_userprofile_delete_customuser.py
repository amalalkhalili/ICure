# Generated by Django 4.2.16 on 2024-12-16 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
