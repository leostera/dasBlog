from forms import *

def common_forms(request):
	return {'search_form':SearchForm(),
			'login_form':HiddenAdminForm(),}
