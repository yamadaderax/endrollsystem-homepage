from django.db import models

# Create your models here.
class Profile(models.Model):

    prof = models.TextField(
                            max_length=1000,
                            verbose_name='profile',
                            default='ここにPROFILE欄に記載する内容を書いて\
                            保存してください',
                            blank=False
                            )



    update_at = models.DateTimeField(
                                     auto_now_add=True,
                                     )

    def __str__(self):
        self.name = 'profile'
        return self.name

class Image(models.Model):
    name = models.CharField(
                            max_length=100,verbose_name='画像の名前'
                            )

    image = models.ImageField(
                              upload_to='images/',
                              verbose_name='画像'
                              )

    def __str__(self):
        return self.name


class Suchedule(models.Model):

    img = models.ForeignKey(
                            Image,
                            on_delete=models.PROTECT,
                            blank=True,
                            null=True,
                            verbose_name='イベントの画像（空白可）'
                            )


    name = models.CharField(
                            max_length=299,
                            blank=False,
                            verbose_name='イベント名'
    )

    live_date = models.DateTimeField(
                                     verbose_name='日時',
                                     blank=False,
                                     )

    place = models.CharField(
                             max_length=500,
                             verbose_name='場所',
                             blank=False,
                             )


    pickup = models.BooleanField(verbose_name='Pick up')

    url = models.URLField()

    def __str__(self):
        return self.name


class Music(models.Model):
    name = models.CharField(
                            verbose_name='曲名',
                            max_length=199,
                            )

    url = models.URLField(verbose_name='URL(空白可)',
                          blank=True,
                          null=True,
                          )
    relese = models.DateField(verbose_name='リリース日')

    kashi = models.TextField(verbose_name='歌詞（空白可）',blank=True,null=True,)

    def __str__(self):
        return self.name


class Disc(models.Model):
    ########################
    # ここのデフォルト画像を後で編集。
    img = models.ForeignKey(Image, on_delete=models.PROTECT, default=None)

    name = models.CharField(
                            max_length=199,
                            verbose_name='CDの名前',
                            blank=False,
                            )

    show_at_home = models.BooleanField(default=False)
    music1 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk1', blank=False, verbose_name='1曲目(二曲目以降は空白可)')
    music2 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk2',  blank=True, verbose_name='2曲目', null=True)
    music3 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk3',  blank=True, verbose_name='3曲目', null=True)
    music4 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk4',  blank=True, verbose_name='4曲目', null=True)
    music5 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk5',  blank=True, verbose_name='5曲目', null=True)
    music6 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk6',  blank=True, verbose_name='6曲目', null=True)
    music7 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk7',  blank=True, verbose_name='7曲目', null=True)
    music9 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk9',  blank=True, verbose_name='9曲目', null=True)
    music8 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk8',  blank=True, verbose_name='8曲目', null=True)
    music10 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk10',  blank=True, verbose_name='10曲目', null=True)
    music11 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk11',  blank=True, verbose_name='11曲目', null=True)
    music12 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk12',  blank=True, verbose_name='12曲目', null=True)
    music13 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk13',  blank=True, verbose_name='13曲目', null=True)
    music14 = models.ForeignKey(Music,on_delete=models.PROTECT,  related_name='disk14', blank=True, verbose_name='14曲目', null=True)
    music15 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk15',  blank=True, verbose_name='15曲目', null=True)
    music16 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk16',  blank=True, verbose_name='16曲目', null=True)
    music17 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk17',  blank=True, verbose_name='17曲目', null=True)
    music18 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk18',  blank=True, verbose_name='18曲目', null=True)
    music19 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk19',  blank=True, verbose_name='19曲目', null=True)
    music20 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk20',  blank=True, verbose_name='20曲目', null=True)
    music21 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk21',  blank=True, verbose_name='21曲目', null=True)
    music22 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk22',  blank=True, verbose_name='22曲目', null=True)
    music23 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk23',  blank=True, verbose_name='23曲目', null=True)
    music24 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk24',  blank=True, verbose_name='24曲目', null=True)
    music25 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk25',  blank=True, verbose_name='25曲目', null=True)
    music26 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk26',  blank=True, verbose_name='26曲目', null=True)
    music27 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk27',  blank=True, verbose_name='27曲目', null=True)
    music28 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk28',  blank=True, verbose_name='28曲目', null=True)
    music29 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk29',  blank=True, verbose_name='29曲目', null=True)
    music30 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk30',  blank=True, verbose_name='30曲目', null=True)
    music31 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk31',  blank=True, verbose_name='31曲目', null=True)
    music32 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk32',  blank=True, verbose_name='32曲目', null=True)
    music34 = models.ForeignKey(Music,on_delete=models.PROTECT,  related_name='disk33', blank=True, verbose_name='34曲目', null=True)
    music33 = models.ForeignKey(Music,on_delete=models.PROTECT, related_name='disk34',  blank=True, verbose_name='33曲目', null=True)
    music35 = models.ForeignKey(Music,on_delete=models.PROTECT,  related_name='disk35', blank=True, verbose_name='35曲目', null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    name = models.CharField(
                            max_length=199,
                            verbose_name='動画のタイトル'
                            )
    url = models.URLField(verbose_name='動画のURL(Youtube)')

    discript = models.TextField(
                                max_length=1000,
                                verbose_name='動画の説明（空白可）',
                                blank=True,
                                null=True,
                                )

    def __str__(self):
        return self.name
