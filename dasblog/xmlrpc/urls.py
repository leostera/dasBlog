from django.conf.urls.defaults import patterns, include, url
from django.contrib.sites.models import Site

from django.views.generic.simple import direct_to_template

from dasblog.settings import PROTOCOL

extra_context = {'protocol': PROTOCOL,
                 'site': Site.objects.get_current()}

urlpatterns = patterns('',
    url(r'^mwapi.xml$', 'django_xmlrpc.views.handle_xmlrpc',name="mwapi"),

    url(r'^wlwmanifest.xml$','direct_to_template',
                           {'template': 'dasblog/xmlrpc/wlwmanifest.xml',
                            'mimetype': 'application/wlwmanifest+xml',
                            'extra_context': extra_context},
                           name='wlwmanifest'),
)
