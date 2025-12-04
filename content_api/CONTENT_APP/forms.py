from django import forms
from django.contrib.auth.models import User
from .models import ContentItem

class LoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username or Email",
        "class": "login-field"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "login-field"
    }))



class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
        }

class ContentItemForm(forms.ModelForm):
    class Meta:
        model = ContentItem
        fields = ["title", "body"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Title",
                "class": "input-field"
            }),
            "body": forms.Textarea(attrs={
                "placeholder": "Description",
                "class": "input-field textarea-field"
            }),
        }
