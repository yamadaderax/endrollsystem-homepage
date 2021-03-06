# Generated by Django 2.1.4 on 2019-02-09 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199, verbose_name='CDの名前')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='画像の名前')),
                ('image', models.ImageField(upload_to='images/', verbose_name='画像')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199, verbose_name='動画のタイトル')),
                ('url', models.URLField(verbose_name='動画のURL(Youtube)')),
                ('discript', models.TextField(blank=True, max_length=1000, verbose_name='動画の説明（空白可）')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=199, verbose_name='曲名')),
                ('url', models.URLField(blank=True, verbose_name='URL(空白可)')),
                ('relese', models.DateField(verbose_name='リリース日')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof', models.TextField(default='ここにPROFILE欄に記載する内容を書いて                            保存してください', max_length=1000, verbose_name='profile')),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=299, verbose_name='イベント名')),
                ('live_date', models.DateTimeField(verbose_name='日時')),
                ('place', models.CharField(max_length=500, verbose_name='場所')),
                ('pickup', models.BooleanField(verbose_name='Pick up')),
                ('url', models.URLField()),
                ('img', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='_html.Image', verbose_name='イベントの画像（空白可）')),
            ],
        ),
        migrations.AddField(
            model_name='disc',
            name='img',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='_html.Image'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='disk1', to='_html.Music', verbose_name='1曲目(二曲目以降は空白可)'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music10',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk10', to='_html.Music', verbose_name='10曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music11',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk11', to='_html.Music', verbose_name='11曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music12',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk12', to='_html.Music', verbose_name='12曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music13',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk13', to='_html.Music', verbose_name='13曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music14',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk14', to='_html.Music', verbose_name='14曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music15',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk15', to='_html.Music', verbose_name='15曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music16',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk16', to='_html.Music', verbose_name='16曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music17',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk17', to='_html.Music', verbose_name='17曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music18',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk18', to='_html.Music', verbose_name='18曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music19',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk19', to='_html.Music', verbose_name='19曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk2', to='_html.Music', verbose_name='2曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music20',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk20', to='_html.Music', verbose_name='20曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music21',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk21', to='_html.Music', verbose_name='21曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music22',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk22', to='_html.Music', verbose_name='22曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music23',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk23', to='_html.Music', verbose_name='23曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music24',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk24', to='_html.Music', verbose_name='24曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music25',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk25', to='_html.Music', verbose_name='25曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music26',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk26', to='_html.Music', verbose_name='26曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music27',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk27', to='_html.Music', verbose_name='27曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music28',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk28', to='_html.Music', verbose_name='28曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music29',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk29', to='_html.Music', verbose_name='29曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk3', to='_html.Music', verbose_name='3曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music30',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk30', to='_html.Music', verbose_name='30曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music31',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk31', to='_html.Music', verbose_name='31曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music32',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk32', to='_html.Music', verbose_name='32曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music33',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk34', to='_html.Music', verbose_name='33曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music34',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk33', to='_html.Music', verbose_name='34曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music35',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk35', to='_html.Music', verbose_name='35曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music4',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk4', to='_html.Music', verbose_name='4曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music5',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk5', to='_html.Music', verbose_name='5曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music6',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk6', to='_html.Music', verbose_name='6曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music7',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk7', to='_html.Music', verbose_name='7曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music8',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk8', to='_html.Music', verbose_name='8曲目'),
        ),
        migrations.AddField(
            model_name='disc',
            name='music9',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='disk9', to='_html.Music', verbose_name='9曲目'),
        ),
    ]
