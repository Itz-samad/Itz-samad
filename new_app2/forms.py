import email
from turtle import title
from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Type Something'}))
    subject = forms.CharField(label='Subject Description', max_length=200, widget= forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type more'}))
    email =  forms.CharField(label='Email', min_length=1, widget=forms.TextInput(attrs={'class':'form-control'}))