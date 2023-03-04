from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm,UserCreationForm
from django.contrib import messages
from . forms import RegistrationForm
# Create your views here.
# def salon(request):
#   template = loader.get_template('login.html')
#   return HttpResponse(template.render())
def salon(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # Replace 'home' with the name of your home page
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#sign up page view
def signup_view(request):
    if request.method == 'GET':
        
        form = RegistrationForm()
        return render(request,'signup.html',{'form': form}) # redirect to login page
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'you have succefully registered')
            login(request,  user)
            return redirect(request,'signup.html',{'form': form})

    else:
            
      return render(request, 'signup.html', {'form': form})

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Check your email to reset your password.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})