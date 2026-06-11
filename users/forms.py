from django import forms
from .models import User, Post
import hashlib


def hash_password(raw):
    return hashlib.sha256(raw.encode()).hexdigest()


class RegisterForm(forms.Form):
    first_name       = forms.CharField(max_length=100)
    last_name        = forms.CharField(max_length=100)
    email            = forms.EmailField()
    username         = forms.CharField(max_length=150)
    password         = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('confirm_password'):
            raise forms.ValidationError("Passwords do not match.")
        if User.objects.filter(username=cleaned.get('username')).exists():
            raise forms.ValidationError("Username already taken.")
        if User.objects.filter(email=cleaned.get('email')).exists():
            raise forms.ValidationError("Email already registered.")
        return cleaned


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = ['text']
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'placeholder': "What's on your mind?"})}
        labels  = {'text': 'Write your post'}
