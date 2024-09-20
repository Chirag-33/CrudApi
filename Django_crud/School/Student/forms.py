from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . models import Record
from django.forms.widgets import PasswordInput,TextInput

from django import forms

#Registering a user 

class CreateUserForm(UserCreationForm):
    class meta:

        model= User
        fields = ['username','password1','password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=300,widget=TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(max_length=20,widget=PasswordInput())


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']