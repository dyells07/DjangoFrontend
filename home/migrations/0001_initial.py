# Generated by Django 4.1.7 on 2023-04-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
