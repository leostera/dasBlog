import datetime

from django.contrib import admin

from models import *

#models.Post
class PostAdmin(admin.ModelAdmin):
	"""
	Admin panel configuration for Posts.
	"""
	
	change_form_template = 'dasblog/admin/post/change_form.html'
	add_form_template	 = 'dasblog/admin/post/change_form.html'

	list_display = (
		'title',
		'slug',
		'published',		
		'deleted',
		'comment_enabled',
		'pub_date',
		'last_update',)
	
	filter_horizontal = ['tags','categories']

	prepopulated_fields = {'slug':['title']}

	exclude = ['last_update','body']
	actions = ['make_published']

	def make_published(self, request, queryset):
		rows_updated = queryset.update(published=1,pub_date=datetime.datetime.now())
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully published." % message_bit)
	make_published.short_description = "Publish selected posts"


# models.Tag
class TagAdmin(admin.ModelAdmin):
	"""
	Admin panel configuration for Tags.
	"""

	list_display = ('title','slug',)
	prepopulated_fields = {'slug':['title']}

# models.Category
class CategoryAdmin(admin.ModelAdmin):
	"""
	Admin panel configuration for Categories.
	"""
	list_display = ('title', 'slug', 'description',)
	prepopulated_fields = {'slug':['title']}

# models.Attachment
class AttachmentAdmin(admin.ModelAdmin):
	"""
	Admin panel configuration for Attachments.
	"""
	list_display = (
		'name',
		'slug',
		'date',
		'media')

	prepopulated_fields = {'slug':['name']}

# Register models with their respective configurations
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Attachment,AttachmentAdmin)