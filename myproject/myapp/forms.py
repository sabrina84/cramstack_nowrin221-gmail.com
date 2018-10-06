from django import forms

class getInfo(forms.Form):
    name  = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    repass = forms.CharField(widget=forms.PasswordInput())


class getLoginInfo(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class getContactInfo(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    image = forms.ImageField()

class editContactInfo(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    email = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=50, required=False)
    image = forms.ImageField(required=False)
