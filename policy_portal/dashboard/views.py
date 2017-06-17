from django.shortcuts import render
from .forms import phase_1Form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.conf import settings
from django.forms import ModelForm
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
	return render (request, 'dashboard.html')

def phase_1_upload(request):
	if request.user.is_authenticated():
		if request.method =='POST':
			form = phase_1Form (request.POST, request.FILES)
			if form.is_valid():
				print(form)
				member_phase1 = form.save(commit=False)
				member_phase1.team = request.user
				member_phase1.save()
			return HttpResponse('Files uploaded')
		else:
			form = phase_1Form()
		return render (request, 'phase_1Form.html', {
			'form':form})