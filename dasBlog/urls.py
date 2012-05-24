from django.conf.urls.defaults import patterns, include, url

import views
from feeds import LatestPostsFeed

urlpatterns = patterns('',
    url(r'^rss-latest.xml$', LatestPostsFeed(), name="rss_feed"),

    url(r'^meta/', include('dasBlog.xmlrpc.urls')),

    url(r'^search/$', views.SearchFormView.as_view(), name="search_page"),

    (r'^comments/', include('django.contrib.comments.urls')),    

    url(r'^tag/(?P<slug>[a-z-]+)/$', views.TagDetailView.as_view(), name="tag_posts"),

    url(r'^category/(?P<slug>[a-z-]+)/$', views.CategoryDetailView.as_view(), name="category_posts"),    

    url(r'^(?P<slug>[a-z-]+)/$', views.PostDetailView.as_view(), name="blog_post"),    

    url(r'^$', views.PostListView.as_view(), name="blog_index"),
)