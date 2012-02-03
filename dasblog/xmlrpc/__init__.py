# METAWEBLOG API CONFIGURATION
XMLRPC_GET_TEMPLATE = "dasblog/xmlrpc/get.html"

XMLRPC_PINGBACK = [
    ('dasblog.xmlrpc.pingback.pingback_ping',				        'pingback.ping'),
    ('dasblog.xmlrpc.pingback.pingback_extensions_get_pingbacks',   'pingback.extensions.getPingbacks')
    ]

XMLRPC_METAWEBLOG = [
    ('dasblog.xmlrpc.metaweblog.get_users_blogs',   'blogger.getUsersBlogs'),
    ('dasblog.xmlrpc.metaweblog.get_user_info',     'blogger.getUserInfo'),
    ('dasblog.xmlrpc.metaweblog.delete_post',     	'blogger.deletePost'),
    ('dasblog.xmlrpc.metaweblog.get_authors',     	'wp.getAuthors'),    
    ('dasblog.xmlrpc.metaweblog.get_categories',    'metaWeblog.getCategories'),    
    ('dasblog.xmlrpc.metaweblog.new_category',      'wp.newCategory'),
    ('dasblog.xmlrpc.metaweblog.get_recent_posts',  'metaWeblog.getRecentPosts'),
    ('dasblog.xmlrpc.metaweblog.get_post',          'metaWeblog.getPost'),
    ('dasblog.xmlrpc.metaweblog.new_post',     		'metaWeblog.newPost'),
    ('dasblog.xmlrpc.metaweblog.edit_post',     	'metaWeblog.editPost'),
    ('dasblog.xmlrpc.metaweblog.new_media_object',	'metaWeblog.newMediaObject')
    ]

XMLRPC_METHODS = XMLRPC_PINGBACK + XMLRPC_METAWEBLOG