# Common imports for urls
from django.conf.urls.defaults import patterns, include, url

# Django admin url imports
from django.contrib import admin
admin.autodiscover()

# Import RedirecView used in url(r'^$')
from django.views.generic import RedirectView

# Import development settings
from blog.dev import settings

urlpatterns = patterns('',
	# Admin "View on site" link fix
	(r'^r/', include('django.conf.urls.shortcut')),

	# Redirect from / to /blog/
    url(r'^$', RedirectView.as_view(url='blog',permanent=True) ),
	
	# Das Blog urls
    url(r'^blog/', include('blog.dasblog.urls')),

    # Media files serving
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
			'document_root': settings.MEDIA_ROOT,}, name='media'),
	
	# Media files serving by slug
	#url(r'^media/slug/(?P<path>.*)$', 'django.views.static.serve', {
	#		'document_root': settings.MEDIA_ROOT,}, name='media'),

	# Django Admin Site urls    
    url(r'^admin/', include(admin.site.urls), name='admin_panel'),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)