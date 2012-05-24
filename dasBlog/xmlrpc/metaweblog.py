"""XML-RPC methods for dasBlog metaWeblog API"""
import os
from datetime import datetime
from xmlrpclib import Fault
from xmlrpclib import DateTime

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.utils.translation import gettext as _
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.template.defaultfilters import slugify, removetags, safe

from blog.django_xmlrpc.decorators import xmlrpc_func

from blog.dasBlog.models     import Post, Category
from blog.dasBlog.settings   import PROTOCOL, HTML_TAGS

# http://docs.nucleuscms.org/blog/12#errorcodes
LOGIN_ERROR = 801
PERMISSION_DENIED = 803

def authenticate(username, password, permission=None):
    """Authenticate staff_user with permission"""
    try:
        user = User.objects.get(username__exact=username)
    except User.DoesNotExist:
        raise Fault(LOGIN_ERROR, _('Username is incorrect.'))
    if not user.check_password(password):
        raise Fault(LOGIN_ERROR, _('Password is invalid.'))
    if not user.is_staff or not user.is_active:
        raise Fault(PERMISSION_DENIED, _('User account unavailable.'))
    if permission:
        if not user.has_perm(permission):
            raise Fault(PERMISSION_DENIED, _('User cannot %s.') % permission)
    return user


def blog_structure(site):
    """A blog structure"""
    return {'url': '%s://%s%s'
            % ( PROTOCOL, site.domain, reverse('blog_index')),
            'blogid': settings.SITE_ID,
            'blogName': site.name}


def user_structure(user, site):
    """An user structure"""
    return {'userid': user.pk,
            'email': user.email,
            'nickname': user.username,
            'lastname': user.last_name,
            'firstname': user.first_name,
            'url': '%s://%s%s' % (
                PROTOCOL, site.domain,
                reverse('blog_index')
                )
            }


def author_structure(user):
    """An author structure"""
    return {'user_id': user.pk,
            'user_login': user.username,
            'display_name': user.username,
            'user_email': user.email}


def category_structure(category, site):
    """A category structure"""
    return {'description': category.title,
            'htmlUrl': '%s://%s%s' % (
                PROTOCOL, site.domain,
                'category/'),
            'rssUrl': '',
            'categoryId': category.pk,
            'parentId': 0,
            'categoryDescription': category.description,
            'categoryName': category.title}

def tag_structure(tag, site):
    """A tag structure"""
    return {}

def post_structure(entry, site):
    """A post structure with extensions"""
    author = User.objects.get(pk=2)
    return {'title': entry.title,
            'description': unicode(entry.html_body),
            'link': '%s://%s%s' % (PROTOCOL, site.domain,
                                   reverse('blog_post',args=[entry.slug])
                                   ),
            # Basic Extensions
            'permaLink': '%s://%s%s' % (PROTOCOL, site.domain,
                                        entry.get_absolute_url()),
            'categories': [cat.title for cat in entry.categories.all()],
            'tags': [tag.title for tag in entry.tags.all()],
            'dateCreated': DateTime(entry.pub_date.isoformat()),
            'postid': entry.pk,
            'userid': author.username,
            'mt_allow_comments': int(entry.comment_enabled),
            'wp_slug': entry.slug,
            }


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_users_blogs(apikey, username, password):
    """blogger.getUsersBlogs(api_key, username, password)
    => blog structure[]"""
    authenticate(username, password)
    site = Site.objects.get_current()
    return [blog_structure(site)]


@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_user_info(apikey, username, password):
    """blogger.getUserInfo(api_key, username, password)
    => user structure"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return user_structure(user, site)


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_authors(apikey, username, password):
    """wp.getAuthors(api_key, username, password)
    => author structure[]"""
    authenticate(username, password)
    return [author_structure(author)
            for author in User.objects.filter(is_staff=True)]


@xmlrpc_func(returns='boolean', args=['string', 'string',
                                      'string', 'string', 'string'])
def delete_post(apikey, post_id, username, password, publish):
    """blogger.deletePost(api_key, post_id, username, password, 'publish')
    => boolean"""
    user = authenticate(username, password)
    entry = Post.objects.get(id=post_id)
    entry.delete()
    return True


@xmlrpc_func(returns='struct', args=['string', 'string', 'string'])
def get_post(post_id, username, password):
    """metaWeblog.getPost(post_id, username, password)
    => post structure"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return post_structure(Post.objects.get(id=post_id), site)


@xmlrpc_func(returns='struct[]',
             args=['string', 'string', 'string', 'integer'])
def get_recent_posts(blog_id, username, password, number):
    """metaWeblog.getRecentPosts(blog_id, username, password, number)
    => post structure[]"""
    user = authenticate(username, password)
    site = Site.objects.get_current()
    return [post_structure(entry, site) \
            for entry in Post.objects.all()[:number]]


@xmlrpc_func(returns='struct[]', args=['string', 'string', 'string'])
def get_categories(blog_id, username, password):
    """metaWeblog.getCategories(blog_id, username, password)
    => category structure[]"""
    authenticate(username, password)
    site = Site.objects.get_current()
    return [category_structure(category, site) \
            for category in Category.objects.all()]


@xmlrpc_func(returns='string', args=['string', 'string', 'string', 'struct'])
def new_category(blog_id, username, password, category_struct):
    """wp.newCategory(blog_id, username, password, category)
    => category_id"""
    authenticate(username, password)
    category_dict = {'title': category_struct['name'],
                     'description': category_struct['description'],
                     'slug': category_struct['slug']}
    category = Category.objects.create(**category_dict)

    return category.pk


@xmlrpc_func(returns='string', args=['string', 'string', 'string',
                                     'struct', 'boolean'])
def new_post(blog_id, username, password, post, publish):
    """metaWeblog.newPost(blog_id, username, password, post, publish)
    => post_id"""
    user = authenticate(username, password)
    if post.get('dateCreated'):
        pub_date = datetime.strptime(
            post['dateCreated'].value.replace('Z', '').replace('-', ''),
            '%Y%m%dT%H:%M:%S')
    else:
        pub_date = datetime.now()

    entry_dict = {'title': post['title'],
                  'body': safe(removetags(post['description'],HTML_TAGS)),
                  'html_body': safe(post['description']),
                  'pub_date': pub_date,
                  'published': 1,
                  'last_update': pub_date,
                  'comment_enabled': post.get('mt_allow_comments', 1) == 1,
                  'slug': slugify(post['title']),
                  }
    entry = Post.objects.create(**entry_dict)

    if 'categories' in post:
        entry.categories.add(*[Category.objects.get_or_create(
                        title=cat, slug=slugify(cat))[0]
                        for cat in post['categories']])
    
    if 'tags' in post:
        entry.tags.add(*[Tag.objects.get_or_create(
                        title=tag, slug=slugify(tag))[0]
                        for tag in post['tags']])

    return entry.pk


@xmlrpc_func(returns='boolean', args=['string', 'string', 'string',
                                      'struct', 'boolean'])
def edit_post(post_id, username, password, post, publish):
    """metaWeblog.editPost(post_id, username, password, post, publish)
    => boolean"""
    user = authenticate(username, password, 'zinnia.change_entry')
    entry = Post.objects.get(id=post_id)
    if post.get('dateCreated'):
        pub_date = datetime.strptime(
            post['dateCreated'].value.replace('Z', '').replace('-', ''),
            '%Y%m%dT%H:%M:%S')
    else:
        pub_date = entry.creation_date

    entry.title = post['title']
    entry.html_body = post['description']
    entry.body = safe(removetags(entry.html_body,HTML_TAGS))
    entry.pub_date = pub_date
    entry.last_update = datetime.datetime.now()
    entry.comment_enabled = post.get('mt_allow_comments', 1) == 1
    entry.slug = 'wp_slug' in post and post['wp_slug'] or slugify(
        post['title'])
    entry.save()

    if 'categories' in post:
        entry.categories.clear()
        entry.categories.add(*[Category.objects.get_or_create(
            title=cat, slug=slugify(cat))[0]
                               for cat in post['categories']])
    
    if 'tags' in post:
        entry.tags.add(*[Tag.objects.get_or_create(
                        title=tag, slug=slugify(tag))[0]
                        for tag in post['tags']])

    return True


@xmlrpc_func(returns='struct', args=['string', 'string', 'string', 'struct'])
def new_media_object(blog_id, username, password, media):
    """metaWeblog.newMediaObject(blog_id, username, password, media)
    => media structure"""
    authenticate(username, password)
    path = default_storage.save(os.path.join(UPLOAD_TO, media['name']),
                                ContentFile(media['bits'].data))
    return {'url': default_storage.url(path)}