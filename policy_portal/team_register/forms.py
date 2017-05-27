from django.forms import ModelForm
from .models import Team, Member
from django import forms
# # our new form
# class RegisterForm(forms.Form):
#     team_name = forms.CharField(required=True)
#     total_members= forms.EmailField(required=True)
#     city= forms.CharField(required=True)
#     state= forms.CharField(required=True)
#     docfile = forms.ImageField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_name','member_email','member_contact', 'id_proof', )

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name','total_members','city', 'state', )