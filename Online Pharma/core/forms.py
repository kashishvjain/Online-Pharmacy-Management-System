from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth import get_user_model
from .models import User



class MyCustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    age = forms.CharField(max_length=30, label='Age')
    phone = forms.CharField(max_length=30, label='Phone Number')
    address = forms.CharField(max_length=30, label='Address')
    gender = forms.CharField(max_length=30,label = 'Gender')
    print('FN',first_name)
    print('Age',age)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.save()
        user.
        return user
