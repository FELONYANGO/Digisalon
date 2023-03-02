from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib import messages

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