# Generated by Django 2.1.4 on 2019-05-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signal',
            name='sid',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='信号强度号'),
        ),
    ]
