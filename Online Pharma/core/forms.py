from django import forms
from allauth.account.forms import SignupForm

GENDER = (
    ('F','Female'),
    ('M','Male'),
    ('O','Other'),
    )


class MyCustomSignupForm(SignupForm):
    age = forms.CharField(max_length=30, label='Age')
    phone = forms.CharField(max_length=30, label='Phone Number')
    address = forms.CharField(max_length=30, label='Address')
    gender = forms.ChoiceField(choices = GENDER,label = 'Gender')
    def signup(self, request, user):
        user.age = self.cleaned_data['age']
        user.phone = self.cleaned_data['phone']
        user.address = self.cleaned_data['address']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user
