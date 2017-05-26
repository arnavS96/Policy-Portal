from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def team_registration(request):
	form_class = RegisterForm
	return render(request, 'team_register_form.html', {'form': form_class,})


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team, Member

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class MemberCreate(CreateView):
	model= Member
	fields = '__all__'





