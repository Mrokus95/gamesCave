from django.shortcuts import render,redirect
from .forms import MyRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy


# Create your views here.
def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False



def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': MyRegisterForm()})
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        log_data = [username, email, password, password2]
        if any(field is "" for field in log_data):
            error = ['Please fill all fields']
            return render(request, 'register.html', {'form': MyRegisterForm(), 'message': error})

        # Checking if password == password2 and email/username not in use
        if password == password2:

            emailIsTaken = User.objects.filter(email=email).exists()
            usernameIsTaken = User.objects.filter(username=username).exists()

            if emailIsTaken and usernameIsTaken:
                error = ['Email and username already taken']
            elif emailIsTaken:
                error = ['Email already taken']
            elif usernameIsTaken:
                error = ['Username already taken']

            if not emailIsTaken and  not usernameIsTaken:
                try:
                    validate_password(password)
                except ValidationError as e:
                    return render(request, 'register.html',{'form': MyRegisterForm(), 'message': e.messages})
                else:
                    emailValid = validate_email(email)
                    if emailValid:
                        form = MyRegisterForm(request.POST)
                        if form.is_valid():
                            inactiveUser = send_verification_email(request, form)
                            message = ['Confirmation email sent.']
                            return render(request, 'register.html',{'form': MyRegisterForm(), 'message': message})
                    else:
                        error = ['Email validation failed']
        else:
            error = ['Password mismatch']
        return render(request, 'register.html',{'form': MyRegisterForm(), 'message': error})

def logInUser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        print(user)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            username = User.objects.filter(username=username).exists()
            if username:
                error = ['Incorrect password']
            else:
                error = ['Invalid or inactive username']
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': error})

def logOutUser(request):
    logout(request)
    return redirect('home')


class CustomPaswordChangeView(PasswordChangeView):
    template_name = "password_change_form.html"
    success_url = reverse_lazy("passwordChangeDone")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_first_name'] = self.request.user.first_name
        return context


class CustomPaswordChangeDoneView(PasswordChangeDoneView):
    template_name = "password_change_done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_first_name'] = self.request.user.first_name
        return context
