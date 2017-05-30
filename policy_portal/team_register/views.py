from django.shortcuts import render
from .forms import TeamForm, MemberForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Team
from django.contrib.auth.decorators import login_required
from django.db import transaction


def success_team(request):
    return render(request, 'success.html')

def team_register(request):
    print(request.user)
    if request.user.is_authenticated():
        print(request.method)
        if request.method == 'POST':
            form = TeamForm(request.POST, user=request.user)\

            #print(form.is_valid())# this is weird kuch to print hona chaieh cosole me Sir iyou know.Thats why dusra option try kar rha tha that i found online.Let me show it to 
            if form.is_valid():
            
                
                team= form.save(commit=False)
                print(team) 
                team.team_admin=request.users
                team.save()
                return redirect('success_team')
        else:
            form = TeamForm()
        return render(request, 'team_register_form.html', {
            'form': form })
#done ab vo run kr jo savenhi ho rha ok
#sir admin mein arnavtest nhi bana ok dhekhta hu 

# @login_required
# @transaction.atomic
# def team_register(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         team_form = TeamForm(request.POST, instance=request.user.team)
#         if user_form.is_valid() and team_form.is_valid():
#             user_form.save()
#             team_form.save()
#             # messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('success_team')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         team_form = TeamForm(instance=request.user.team)#change kr teamko ?? yes sir, thoda boht try kar rha tha khud, original version  stackoverflow pe hain.Shall i get it back to that form?, ha do it once Ok
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'team_form': team_form 
#     })
    



def member_register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm()
    return render(request, 'member_register_form.html', {
        'form': form
    })




















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





