from django.contrib import admin

from service import models

# class StoUserAdmin(admin.ModelAdmin):
	# list_display = ('')
	# search_filed = ()

class ChapterAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'parentChapter_ID',
		'sonChapters_ID',
		'author',
		'lovers',
		'enjoy_num',
		)
	list_filter = (
		'name',
		'author',
		'enjoy_num',
		)
	search_filed = ('name')		

class StoryAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'start_author',
		'headchapter',
		'son_num',
		'enjoy_num',
		'part_in_num',
		)
	search_filed = ('name')

admin.site.register(models.StoUser)
admin.site.register(models.Chapter)
admin.site.register(models.Story)
