#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
power_state = (
		(0, u'游客'),
		(1, u'普通用户'),
		(2, u'管理员'),
	)


class StoUser(User):
	power = models.IntegerField()



class Chapter(models.Model):
	name = models.CharField(u'章节名', max_length=63)
	content = models.TextField(u'内容')
	parentChapter_ID = models.IntegerField(u'父章节id',blank=True)
	sonChapters_ID = models.TextField(u'子章节id',blank=True)
	author = models.OneToOneField(StoUser, verbose_name=u'创作者')
	son_num = models.IntegerField(u'子章节数量',default=0)
	image_url = models.URLField(u'图片链接', blank=True)
	enjoy_num = models.IntegerField(u'喜欢人数', default=0)
	lovers = models.ManyToManyField(User,verbose_name=u'喜欢的人')

class Story(models.Model):
	name = models.CharField(u'故事名', max_length=63)
	start_author = models.OneToOneField(StoUser, default=None)
	headchapter = models.OneToOneField(Chapter, verbose_name=u'启动章节')
	son_num = models.IntegerField(u'子章节数量', default=0)
	enjoy_num = models.IntegerField(u'喜欢人数', default=0)
	part_in_num = models.IntegerField(u'参与创作人数', default=0)