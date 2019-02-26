from django import forms

class UserLogin(forms.Form):
    """ form to log in user in """
    
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    