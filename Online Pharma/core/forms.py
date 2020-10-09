from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from .models import User



class MyCustomSignupForm(SignupForm):
    class Meta:
        model = User

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    age = forms.CharField(max_length=30, label='Age')
    phone = forms.CharField(max_length=30, label='Phone Number')
    address = forms.CharField(max_length=30, label='Address')
    gender = forms.CharField(max_length=30,label = 'Gender')



    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.get_profile().age = self.cleaned_data['age']
        user.get_profile().phone = self.cleaned_data['phone']
        user.get_profile().address = self.cleaned_data['address']
        user.get_profile().gender = self.cleaned_data['gender']
        user.save()

        return user
