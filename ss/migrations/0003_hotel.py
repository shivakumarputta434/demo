# Generated by Django 3.1.3 on 2020-11-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ss', '0002_emp1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
