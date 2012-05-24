import forms

def common_forms(request):
	return {'search_form':forms.SearchForm(),
			'login_form':forms.HiddenAdminForm(),}
