from django import forms
from django.contrib.auth import get_user_model
from .models import ContentItem

User = get_user_model()

class LoginForm(forms.Form):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username or Email",
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))



class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
            "username": forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class ContentItemForm(forms.ModelForm):
    class Meta:
        model = ContentItem
        fields = ["title", "body"]

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Title",
                "class": "form-control"
            }),
            "body": forms.Textarea(attrs={
                "placeholder": "Description",
                "class": "form-control",
                "rows": 4
            }),
        }
