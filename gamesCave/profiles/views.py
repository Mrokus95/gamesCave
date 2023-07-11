from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm
from django.http import HttpResponse
from django.views import View


# Create your views here.


@login_required
def editUserDataView(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        msg = "Profil niezaktualizowany - wystąpił bład"
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            msg = "Profil zaktualizowany"
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        msg = ""
    context={"profile_form": profile_form,
             "user_form": user_form,
             "msg": msg}
    return render(request,'edit-profile.html',context)