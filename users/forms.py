from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class EditProfileForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ['address', 'phoneno', 'avatar']


class EditProfileForm(forms.Form):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    avatar = forms.FileField()
    address = forms.CharField(max_length=500)
    phoneno = forms.IntegerField(max_value=9999999999)

