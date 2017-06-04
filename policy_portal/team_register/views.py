from django.shortcuts import render
from .forms import TeamModelForm, MemberForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import TeamModel, Member
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.conf import settings
from django.forms import ModelForm, formset_factory,modelformset_factory, inlineformset_factory

member_number=5;

def success_team(request):
    return render(request, 'success.html')

def registration_successful(request):
    return render(request, 'team_registration_successful.html')




def team_register(request):
    if request.user.is_authenticated():
        
        #if request.method == "POST": 
        if request.method=='POST':
            
            form = TeamModelForm(request.POST)
            if form.is_valid():            
                team= form.save(commit=False)
                member_number=team.total_team_members
                
                team.team_admin=request.user
                # print(member) 
                team.save()
                return redirect('success_team')
        else:
            form = TeamModelForm()
            print(request.user)
        return render(request, 'team_register_form.html', {
            'form': form })


print(member_number)

def member_register(request):
    if request.user.is_authenticated():
        MemberFormSet= formset_factory(MemberForm,extra=member_number)
        if request.method=='POST':
            
            formset = MemberFormSet(request.POST,request.FILES)
            print(formset)
            if formset.is_valid():
                
                for form in formset:
                    if form.is_valid():
                        print(form)
                        member=form.save(commit=False)
                        member.team=request.user
                        member.save()
                        
                return redirect('registration_successful')
        else:
            formset = MemberFormSet()
            
        return render(request, 'member_register_form.html', {
            'formset': formset })












# Create your views here.
# def team_registration(request):
# 	form_class = RegisterForm
# 	if request.method =='POST':
# 		form = RegisterForm(request.POST, request.FILES)
# 		if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('team_registration'))
#     else:
#         form = RegisterForm()  # A empty, unbound form

# 	return render(request, 'team_register_form.html', {'form': form_class,})


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





