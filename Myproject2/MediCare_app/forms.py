from MediCare_app.models import patients, User, Doctors
from django import forms
from django.contrib.auth.forms import UserCreationForm


class user_Registration(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password1','password2')



class patient_RegForm(forms.ModelForm):
    class Meta:
        model=patients
        exclude=('user','patient_id')


class doctor_RegForm(forms.ModelForm):
    class Meta:
        model =Doctors
        exclude = ('user', 'Approve_status')






