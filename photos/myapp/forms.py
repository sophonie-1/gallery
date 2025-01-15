from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User




class LoginForm(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(
        attrs={'placeholder':'shiramwo izina ryawe'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'shiramwo password'}))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not User.objects.filter(username=username).exists():
            raise ValidationError('izina sigyo subiramwo')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        user = User.objects.filter(password=password)
        if not user.exists():
            raise ValidationError('wihenze password subiramwo canke wiyandikishe nyamba arubwambere')
        return password

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=200,widget=forms.TextInput(
        attrs={'placeholder':'izina ukoresha'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder':'email yawe'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'password yawe'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'yisubiremwo password yawe'}))
    
    def clean_username(self):   
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username already exists')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!= password2:
            raise ValidationError('Passwords do not match')
        return password2
    
    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1']
        )
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        exclude = ['username', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

