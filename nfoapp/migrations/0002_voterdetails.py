# Generated by Django 3.1.3 on 2020-12-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoterDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yname', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('rate', models.CharField(max_length=50)),
                ('bewith', models.CharField(max_length=50)),
            ],
        ),
    ]
