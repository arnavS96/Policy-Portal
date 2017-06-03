from django.forms import ModelForm, formset_factory
from .models import TeamModel, Member
from django import forms
from django.contrib.auth.models import User
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

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('member_name','member_email','member_contact','id_proof', )


# MemberFormSet = formset_factory(MemberForm, extra=5)


    # def __init__(self, user, *args, **kwargs):
    # 	super(MemberForm, self).__init__(*args, **kwargs)
    # 	self.fields['team_name'].queryset = TeamModel.objects.filter(user=user)

class TeamModelForm(forms.ModelForm):
    class Meta:
        model = TeamModel
        fields = ('team_name','total_members','city', 'state', )
# 