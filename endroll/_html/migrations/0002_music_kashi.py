# Generated by Django 2.1.4 on 2019-02-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_html', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='kashi',
            field=models.TextField(blank=True, verbose_name='歌詞（空白可）'),
        ),
    ]
