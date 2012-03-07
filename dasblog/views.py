# Import datetime module
import datetime
# Import regular expresions module
import re

# Import some generic views
from django.views.generic import DetailView, ListView, FormView
# Import the RequestContext to be used in the FormView
from django.template import RequestContext
# Import some shortcuts
from django.shortcuts import render_to_response
# Import the magical Q 
from django.db.models import Q

# Import all models from DasBlog
from models import *
# Import all forms from DasBlog
from forms	import *

class SearchFormView(FormView):
	"""
	FormView inherited class representing the fancy search form used in the overlay search
	bar. Propierties:

	-template_name			the template object used to render the results.

	-context_object_name	the name of the context object in the template.

	-form_class				the form model.

	"""

	template_name 		= 'dasblog/search_results.html'
	context_object_name = 'results'
	form_class 			= SearchForm

	def get_context_data(self, **kwargs):
		"""
		Perform a search looking for matches in categories, tags, posts and attachments.
		Returns a context dictionary with all the objects retrieved.
		"""

		# Try to get the query, otherwise make it an empty string
		query = self.request.POST.get('string','')
		# If it's not empty
		if( query != '' ):
			# Check if it's a match for regular expresion ^(\w{3}) (\d{1,2}?)$
			# For example, JAN 2
			if( re.match(r"^(\w{3}) (\d{1,2}?)$",query)):
				# If it is, format it accordingly
				query = datetime.datetime.strptime("2012 %s" % query.lower(),"%Y %b %j").date()				
			elif( re.match(r"^(\w{3})-(\d{1,2}?)$",query)):
				# Check for same regex but with a dash (-) instead of a space
				# Between the letters and the numbers
				# If it is, format the query accordingly
				query = datetime.datetime.strptime("2012-%s" % query.lower(),"%Y-%b-%j").date()
			
			# Now retrieve all the objects performing OR queries with ILIKE
			self.categories = Category.objects.filter(Q(title__icontains=query)|Q(description__icontains=query))
			self.tags  		= Tag.objects.filter(title__icontains=query)
			# Only retrieve published, non-deleted posts
			self.posts		= Post.objects.filter(published__exact=True,deleted__exact=False).filter(Q(title__icontains=query)|Q(body__icontains=query)|Q(pub_date__icontains=query))
			# TO DO: Enable attachments properly.	
			#self.attachs 	= Attachment.objects.filter(Q(name__icontains=query)|Q(date__icontains=query))

		# Now call superclass method to retrieve the base dictionary
		context = super(SearchFormView, self).get_context_data(**kwargs)	

		# Check if none of the querysets has items
		if( not self.categories and
			not self.tags and
			#not self.attachs and
			not self.posts ):
			# And kick the template in the ass
			context['go_to_hell'] = True
		else:
			# Otherwise, fullfil the context nicely :)
			context['categories'] 	= self.categories
			context['tags']			= self.tags
			context['posts'] 		= self.posts
			#context['attachs'] 	= self.attachs
	
		# Return the filled context dictionary.
		return context

	def form_valid(self, form):
		"If the form is valid, execute the query while rendering it in the specified template"
		return render_to_response(self.template_name,RequestContext(self.request,self.get_context_data(form=form),))

	def form_invalid(self, form):
		"This is rarely going to happen, so anyway I just return form_valid."
		return self.form_valid(form)

class PostDetailView(DetailView):
	template_name		= 'dasblog/post/details.html'
	context_object_name	= 'post'
		
	def get_object(self):
		# Get Post by slug only if it has been published and it is not deleted
		self.queryset = Post.objects.filter(slug__exact=self.kwargs['slug'],published__exact=True,deleted__exact=False)
		# Call the superclass
		object = super(PostDetailView, self).get_object()
		# Return the object
		return object
	
	def get_context_data(self, **kwargs):
		context = super(PostDetailView,self).get_context_data(**kwargs)
		return RequestContext(self.request,context)

class TagDetailView(DetailView):
	template_name		= 'dasblog/tag/posts.html'
	context_object_name	= 'tag'
		
	def get_object(self):
		self.queryset = Tag.objects.filter(slug__exact=self.kwargs['slug'])
		# Call the superclass
		object = super(TagDetailView, self).get_object()
		# Return the object
		return object
	
	def get_context_data(self, **kwargs):
		context = super(TagDetailView,self).get_context_data(**kwargs)
		return context	

class CategoryDetailView(DetailView):
	template_name		= 'dasblog/category/posts.html'
	context_object_name	= 'category'
		
	def get_object(self):
		self.queryset = Category.objects.filter(slug__exact=self.kwargs['slug'])
		# Call the superclass
		object = super(CategoryDetailView, self).get_object()
		# Return the object
		return object
	
	def get_context_data(self, **kwargs):
		context = super(CategoryDetailView,self).get_context_data(**kwargs)
		return context		
	
class PostListView(ListView):
	template_name		= 'dasblog/post/list.html'
	context_object_name	= 'posts'
	queryset = Post.objects.filter(published__exact=True,deleted__exact=False)

	def get_context_data(self, **kwargs):
		context = super(PostListView,self).get_context_data(**kwargs)
		return context