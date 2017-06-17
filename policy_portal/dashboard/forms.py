from django.forms import ModelForm
from .models import phase_1
#from .models import test_image
from django import forms
# our new form

class phase_1Form(forms.ModelForm):
    class Meta:
        model = phase_1
        fields =('problem_images','problem_images_upload','FIR_number','FIR_upload','news_articles_number','news_articles_upload','miscellaneous_upload','miscellaneous_detail',)

#class test_form(forms.Form):
#	testing_upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))