import email
from email import message
from django import forms
from pkg_resources import require

class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your e-mail address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    