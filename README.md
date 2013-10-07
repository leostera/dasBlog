#das Blog (discontinued)
###For blogging wasn't german enough.

Hi there guys, this is a little blog made with Django 1.3 and _being ported_ to 1.4 that is capable of:
* Post managing
* Comments
* Tags and categories
* Keyword searching for tags, categories and comments
* Works with some XMLRPC capabilities too
* Syndication

_Porting is a WIP so it might not work out of the box yet_

###Ingredients

It was a bit of a show & tell some time ago, so to keep that spirit alive here's a list of what this app uses:
* Models that extend the base model class functionality and use it's hooks
* Views classes inheriting from FormView, DetailView and ListView
* Nested and extended templates
* Context processors
* RegEx Grouped Patterns for URL matching incluiding variable extraction
* Forms, the regular kind and the admin kind.
* Admin panel registration for models incluiding extending the functionality and use of hooks
* Use of urllibs, thou most of the XMLRPC was inspired by Zinnia.

###Installation

You'll need Django (>1.3) and django_xmlrpc.

###Notes

I'm no longer maintainning this repository after this has been fully ported to Django 1.4, yet you are welcomed and encouraged to clone it, fork it, use it and in the best case, learn something new.

#License
Copyright &copy; 2112 Leandro Ostera.
For further details read the LICENSE file.
