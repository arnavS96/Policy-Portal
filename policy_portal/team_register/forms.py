from django.forms import ModelForm
from .models import Team, Member
from django import forms
# our new form
class RegisterForm(forms.Form):
    team_name = forms.CharField(required=True)
    total_members= forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
        