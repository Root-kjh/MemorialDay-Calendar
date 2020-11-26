from django import forms
from .models import User
import hashlib

HASH_SALT = "KJH_MEMORIAL"

def HASH_PASSWORD(password):
    hashed_password = hashlib.sha512(str(password+HASH_SALT).encode('utf-8')).hexdigest()
    return hashed_password


class SignupForm(forms.ModelForm):
    verify_password = forms.CharField(label= 'Verify Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = {'user_id', 'user_password', 'verify_password'}
        widgets = {
            'user_password' : forms.PasswordInput(),
        }
        labels = {
            'user_id' : 'ID',
            'user_password' : 'Password',
            'verify_password' : 'Verify Password',
        }
    field_order = ['user_id', 'user_password', 'verify_password']
    
    def clean_verify_password(self):
        password1 = self.cleaned_data.get('user_password')
        password2 = self.cleaned_data.get('verify_password')
        if password1 != password2:
            raise forms.ValidationError('Password must match')
        return password2

    def save(self, commit=True):
        user_id_count = User.objects.filter(user_id = self.cleaned_data['user_id']).count()
        if user_id_count==0:
            user = User(
                user_id = self.cleaned_data['user_id'], 
                user_password = HASH_PASSWORD(self.cleaned_data['user_password']))
            if commit:
                user.save()
            return user
        else:
            raise forms.ValidationError('Exist User ID')

        
class SigninForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'user_id', 'user_password'}
        widgets = {
            'user_password' : forms.PasswordInput(),
        }
        labels = {
            'user_id' : 'ID',
            'user_password' : 'Password',
        }
    field_order = ['user_id', 'user_password']

    def signin(self):
        password = User.objects.filter(user_id=self.cleaned_data['user_id'])[0].user_password
        if password != HASH_PASSWORD(self.cleaned_data['user_password']):
            raise forms.ValueError('Login failed')
        else:
            return self.cleaned_data['user_id']


class PasswordModifyForm(forms.ModelForm):
    new_password = forms.CharField(label= 'New Password', widget=forms.PasswordInput)
    verify_new_password = forms.CharField(label= 'Verify New Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'user_password', 'new_password', 'verify_new_password'}
        widgets = {
            'user_password' : forms.PasswordInput(),
        }
        labels = {
            'user_password' : 'Password',
            'new_password' : 'New Password',
            'verify_new_password' : 'Verify New Password',
        }
    field_order = ['user_password', 'new_password', 'verify_new_password']
    
    def clean_new_password(self):
        password1 = self.cleaned_data.get('new_password')
        password2 = self.cleaned_data.get('verify_new_password')
        if password1 != password2:
            raise forms.ValidationError('New Password must match')
        return password2


class WithdrawForm(forms.ModelForm):
    verify_password = forms.CharField(label= 'Verify Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'user_password', 'verify_password'}
        widgets = {
            'user_password' : forms.PasswordInput(),
        }
        labels = {
            'user_password' : 'Password',
            'verify_password' : 'Verify Password',
        }
    field_order = ['user_password', 'verify_password']
    def clean_verify_password(self):
        password1 = self.cleaned_data.get('user_password')
        password2 = self.cleaned_data.get('verify_password')
        if password1 != password2:
            raise forms.ValidationError('Password must match')
        return password2