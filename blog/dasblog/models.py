from django.db import models

from django.template.defaultfilters import removetags, safe

from dasblog.settings import HTML_TAGS

import datetime

class Tag(models.Model):
	"""
	Tag model
	"""
	class Meta:
		ordering = ['title']	
		pass

	title	= models.CharField(max_length=100,null=False)
	slug	= models.SlugField(unique=True,null=False)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('tag_posts', (), {'slug':self.slug,})

class Category(models.Model):
	"""
	Category model.
	"""
	class Meta:
		verbose_name_plural = u'Categories'	
		ordering = ['title']	
		pass

	title		= models.CharField(max_length=100,null=False)
	slug		= models.SlugField(unique=True,null=False)
	description	= models.CharField(max_length=250)

	def __unicode__(self):
		return self.title
	
	@models.permalink
	def get_absolute_url(self):
		return ('category_posts', (), {'slug':self.slug,})

class Attachment(models.Model):
	"""
	Attachment model. This represents a file uploaded that is being used inside
	a post content, such as an image, codefile, etc. Fields:

	-name:	the name of the attachment.

	-slug:	the slug of the attachment. 
			to be used for easier access to uploaded resources.
		
	-date:	date when it was uploaded.

	-media: the path to the file itself.
	"""
	class Meta:
		ordering = ['-date','name']
		pass
	
	name	= models.CharField(max_length=250)
	slug	= models.SlugField(unique=True,null=False)
	date	= models.DateField(default=datetime.datetime.today())
	media	= models.FileField(max_length=100,upload_to='post-uploads')

# TO DO: add this field and check how it can be auto-populated depending on file type.	
	#mimetype= models.CharField(max_length=100,null=False)

	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return ('media', (), {'path':self.media,})

class Post(models.Model):
	"""
	Post model representing an entry in the blog. Fields:

	-title:				the post title
		
	-slug:				the post slug
	
	-html_body:			body content with html markup
		
	-body:				the content of the post without html markup.
						used for searchs.

	-published:			if true, the post is published. if false, it is a draft

	-deleted:			if true, the post was deleted and will not be shown anywhere.

	-last_update:		keeps track of the latest 'touch' of the document, even if
						it is a draft.

	-pub_date:			date in which the post was originally published.

	-comment_enabled:	if true then the comment form will be enabled in the posts
						detailed view.

	-tags:				m2m field for the tags this post has

	-categories:		m2m field for the categories this post has

	-attachments:		m2m field for the attachments this post has
	"""

	class Meta:
		"""
		Model meta options. Mostly self-explanatory.
		"""
		ordering = ['-pub_date','published','id']
		pass
	
	title 		= models.CharField(max_length=120,null=False)
	slug		= models.SlugField(unique=True,null=False)

	html_body	= models.TextField(null=False)
	body		= models.TextField(null=True)	

	published	= models.BooleanField(default=False)
	deleted		= models.BooleanField(default=False)
	last_update	= models.DateTimeField(default=datetime.datetime.now())
	pub_date	= models.DateField(default=datetime.datetime.today(),null=True)

	comment_enabled = models.BooleanField("Enable Comments",default=True)

	tags		= models.ManyToManyField(Tag)
	categories 	= models.ManyToManyField(Category)
	attachments = models.ManyToManyField(Attachment,null=True)	

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('blog_post', [], {'slug':self.slug,})

	def save(self, *args, **kwargs):		
		# Clean the body, removing all html tags.
		self.body = safe(removetags(self.html_body,HTML_TAGS))	

	# TO DO #
		# Replace the <attach id="slug"> html tag with proper tags:
		#	for example, <attach id="image-people"> will be replaced with
		#	'<img src="%s"' />' % reverse('media/slug', [], {'slug':"image-people"})
		#   so in the html it displays properly.

		# Then call the *real* save method.
		super(Post, self).save(*args, **kwargs)