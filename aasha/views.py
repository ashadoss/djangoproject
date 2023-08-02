from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')
   
def course_details(request):
    return render(request,'course_details.home')

def courses(request):
    return render(request,'courses.html')

def events(request):
    return render(request,'events.html')

def index(request):
    return render(request,'index.html')

def pricing(request):
    return render(request,'pricing.html')

def trainers(request):
    return render(request,'request.html')    
    
 from django.shortcuts import render, redirect
from appname.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
 


def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('appname:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('appname:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('appname:login_reg')
	return redirect('aasha:home')   