from django.shortcuts import render

# Create your views here.
def index(request):
	return render(
        request,
        'home.html',
     )

def ContactUs(request):
	return render(request,'contact.html',)