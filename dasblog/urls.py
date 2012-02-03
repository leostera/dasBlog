from django.conf.urls.defaults import patterns, include, url

from views import *
from feeds import LatestPostsFeed

urlpatterns = patterns('',
    url(r'^rss-latest.xml$', LatestPostsFeed(), name="rss_feed"),

    url(r'^meta/', include('blog.dasblog.xmlrpc.urls')),

    url(r'^search/$', SearchFormView.as_view(), name="search_page"),

    (r'^comments/', include('django.contrib.comments.urls')),    

    url(r'^tag/(?P<slug>[a-z-]+)/$', TagDetailView.as_view(), name="tag_posts"),

    url(r'^category/(?P<slug>[a-z-]+)/$', CategoryDetailView.as_view(), name="category_posts"),    

    url(r'^(?P<slug>[a-z-]+)/$', PostDetailView.as_view(), name="blog_post"),    

    url(r'^$', PostListView.as_view(), name="blog_index"),
)