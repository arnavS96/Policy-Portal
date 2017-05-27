from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def team_registration(request):
	form_class = RegisterForm
	return render(request, 'team_register_form.html', {'form': form_class,})


	# from django.views.generic.edit import CreateView, UpdateView, DeleteView
	# from django.urls import reverse_lazy
	# from .models import Team, Member

	# class TeamCreate(CreateView):
	#     model = Team
	#     fields = '__all__'

	# class MemberCreate(CreateView):
	# 	model= Member
	# 	fields = '__all__'

# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse





# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = RegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('list'))
#     else:
#         form = RegisterForm()  # A empty, unbound form

    # # Load documents for the list page
    # documents = Document.objects.all()

    # # Render list page with the documents and the form
    # return render(
    #     request,
    #     'list.html',
    #     {'documents': documents, 'form': form}
    # )





