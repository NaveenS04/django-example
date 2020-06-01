from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class User(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileInfodata(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_link','profile_pic')
