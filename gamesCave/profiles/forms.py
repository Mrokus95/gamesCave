from .models import Profile
from django.db.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nick','photo','phone_number','bank_account']