from django.core import validators
from django import forms
from .models import User
from django.forms  import ModelForm

CHOICES = [('M','Male'),('F','Female')]
class Employee(forms.ModelForm):
    gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    class Meta:
        model=User
        fields=('name','pan','age','gender','email','city')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'pan':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }
