# Generated by Django 2.1.4 on 2019-02-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_html', '0004_auto_20190217_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='disc',
            name='show_at_home',
            field=models.BooleanField(default=False),
        ),
    ]
