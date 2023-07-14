from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm
from django.http import HttpResponse
from django.views import View
from .models import Profile


# Create your views here.

@login_required
def editUserDataView(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        nickname = request.POST.get('nick')
        photo = request.POST.get('photo')
        phone_number = request.POST.get('phone_number')
        bank_number = request.POST.get('bank_account')
        msg = []

        if first_name:
            if first_name.isalpha():
                capitalized_first_name = first_name.capitalize()
            else:
                msg.append("Profil niezaktualizowany - imię zawiera niedozwolone znaki")

        if last_name:
            if last_name.isalpha():
                capitalized_last_name = last_name.capitalize()
            else:
                msg.append("Profil niezaktualizowany - nazwisko zawiera niedozwolone znaki")
        
        if phone_number:
            cleared_phone_number = ''.join([sign for sign in phone_number if sign.isdigit()])
            if len(cleared_phone_number) not in [0, 9]:
                msg.append("Profil niezaktualizowany - numer telefonu jest nieprawidłowy")

        if bank_number:
            cleared_bank_number = ''.join([sign for sign in bank_number if sign.isdigit()])
            if len(cleared_bank_number) not in [0, 26]:
                msg.append("Profil niezaktualizowany - numer konta jest nieprawidłowy")

        if msg:
            context={"profile_form": profile_form,
                     "account_type" : request.user.profile.account_type,
             "user_form": user_form,
             "msg": msg}
            return render(request,'edit-profile.html',context)

        if user_form.is_valid() and profile_form.is_valid():
            # Update form data for user model
            updated_user_data = user_form.save(commit=False)
            updated_user_data.first_name = capitalized_first_name
            updated_user_data.last_name = capitalized_last_name
            updated_user_data.save()

            # Update form data for profile model
            updated_profile_data = profile_form.save(commit=False)
            updated_profile_data.phone_number = cleared_phone_number
            updated_profile_data.bank_account = cleared_bank_number
            updated_profile_data.save()
            msg = "Profil zaktualizowany"
        else:
            msg = "Profil niezaktualizowany - błąd formularza"
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        msg = ""
    context={"profile_form": profile_form,
             "user_form": user_form,
             "account_type": request.user.profile.account_type,
             "msg": msg}
    return render(request,'edit-profile.html',context)