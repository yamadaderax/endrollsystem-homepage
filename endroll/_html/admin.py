from django.contrib import admin

from . import models
# Register your models here.
admin.site.site_header = 'END ROLL SYSTEMホームページ管理画面'
admin.site.index_title = 'サイトに表示する情報一覧'
admin.site.register(models.Disc)
admin.site.register(models.Profile)
admin.site.register(models.Movie)
admin.site.register(models.Music)
admin.site.register(models.Suchedule)
admin.site.register(models.Image)
