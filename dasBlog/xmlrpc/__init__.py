# METAWEBLOG API CONFIGURATION
XMLRPC_GET_TEMPLATE = "dasBlog/xmlrpc/get.html"

XMLRPC_PINGBACK = [
    ('dasBlog.xmlrpc.pingback.pingback_ping',				        'pingback.ping'),
    ('dasBlog.xmlrpc.pingback.pingback_extensions_get_pingbacks',   'pingback.extensions.getPingbacks')
    ]

XMLRPC_METAWEBLOG = [
    ('dasBlog.xmlrpc.metaweblog.get_users_blogs',   'blogger.getUsersBlogs'),
    ('dasBlog.xmlrpc.metaweblog.get_user_info',     'blogger.getUserInfo'),
    ('dasBlog.xmlrpc.metaweblog.delete_post',     	'blogger.deletePost'),
    ('dasBlog.xmlrpc.metaweblog.get_authors',     	'wp.getAuthors'),    
    ('dasBlog.xmlrpc.metaweblog.get_categories',    'metaWeblog.getCategories'),    
    ('dasBlog.xmlrpc.metaweblog.new_category',      'wp.newCategory'),
    ('dasBlog.xmlrpc.metaweblog.get_recent_posts',  'metaWeblog.getRecentPosts'),
    ('dasBlog.xmlrpc.metaweblog.get_post',          'metaWeblog.getPost'),
    ('dasBlog.xmlrpc.metaweblog.new_post',     		'metaWeblog.newPost'),
    ('dasBlog.xmlrpc.metaweblog.edit_post',     	'metaWeblog.editPost'),
    ('dasBlog.xmlrpc.metaweblog.new_media_object',	'metaWeblog.newMediaObject')
    ]

XMLRPC_METHODS = XMLRPC_PINGBACK + XMLRPC_METAWEBLOG