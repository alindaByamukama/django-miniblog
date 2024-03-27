from django import forms

class RegisterUser(forms.form):
    username = forms.CharField(label="username", max_length=100)
    email = forms.EmailField(label="email", required=True)
    password = forms.PasswordInput(label="password")
    # submit = forms.