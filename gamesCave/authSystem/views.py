from django.shortcuts import render,redirect
from .forms import MyRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from verify_email.email_handler import send_verification_email
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetView
from django.urls import reverse_lazy
from profiles.models import Profile
from django.utils.http import url_has_allowed_host_and_scheme
from django.http import HttpResponseBadRequest


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
                            profile = Profile.objects.create(user=inactiveUser)
                            return render(request, 'register.html',{'form': MyRegisterForm(), 'message': message})
                    else:
                        error = ['Email validation failed']
        else:
            error = ['Password mismatch']
        return render(request, 'register.html',{'form': MyRegisterForm(), 'message': error})

def logInUser(request):
    if request.method == 'GET':
        return render(request, "login.html", {'form': AuthenticationForm(), 'next': request.GET.get('next', '')})

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            redirect_to = request.POST.get('next', '')
            if redirect_to and url_has_allowed_host_and_scheme(redirect_to, allowed_hosts=None):
                return redirect(redirect_to)
            return redirect('home')
        else:
            username_exists = User.objects.filter(username=username).exists()
            if username_exists:
                error = 'Incorrect password'
            else:
                error = 'Invalid or inactive username'
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': error})

    return HttpResponseBadRequest()

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

class CustomPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("password_reset_done")
    template_name = "password_reset_form.html"
    html_email_template_name = "password_reset_email.html"

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
        success_url = reverse_lazy("password_reset_complete")
        template_name = "password_reset_confirm.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['uidb64'] = self.kwargs['uidb64']
            context['token'] = self.kwargs['token']
            return context

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

