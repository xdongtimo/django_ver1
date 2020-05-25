from django import forms
import re
from django.contrib.auth.models import User

# Create class extend from library: forms.Form and define fields
class RegistrationForm(forms.Form):
    username = forms.CharField(label = 'Account', max_length =30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Pass Word',widget = forms.PasswordInput())
    password2 = forms.CharField(label = 'Confirm Pass Word',widget = forms.PasswordInput())

    # Create function to vadition fields: syntax- [clean_<field name>]
    def clean_password2(self):
            if 'password1' in self.cleaned_data:
                password1 = self.cleaned_data['password1']
                password2 = self.cleaned_data['password2']
                if password1 == password2 and password1:
                    return password2
            raise forms.ValidationError("Pass word is not fit")

    def clean_username(self):
            username = self.cleaned_data['username']
            if not re.search(r'^\w+$', username):
                raise forms.ValidationError("Account name has special characters")
            try:
                User.objects.get(username = username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError("Account already exists")

        # Create function save
    def save(self):
            User.objects.create_user(username=self.cleaned_data['username'],
            email=self.cleaned_data['email'], password =self.cleaned_data['password1'])

