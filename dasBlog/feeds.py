from django.contrib.syndication.views import Feed

from models import Post

import datetime

class CommonFeed(Feed):
	"""
	Common feeds propierties.
	"""
	author_name = "AUTHOR_NAME"
	author_email= "AUTHOR_EMAIL"
	author_link = "AUTHOR_LINK"

class LatestPostsFeed(CommonFeed):	
	"""
	Latests Posts feed. Retrieves the 10 last published non-deleted posts.
	"""
	title = "%s news" % "BLOG_TITLE"
	link = "/blog/"
	description = "Latest posts on %s" % "BLOG_TITLE"

	description_template = "dasBlog/feeds/latest_description.html"	

	def items(self):
		return Post.objects.filter(published__exact=True,deleted__exact=False)[:10]

	def item_title(self, item):
		return item.title

	def item_pubdate(self,item):
		return datetime.datetime(item.pub_date.year,item.pub_date.month,item.pub_date.day)