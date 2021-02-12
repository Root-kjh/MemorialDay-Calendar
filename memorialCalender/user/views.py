from .models import User
from .forms import PasswordModifyForm, SigninForm, SignupForm, WithdrawForm
from django.shortcuts import render, redirect
from django import forms

def signup(request):
    if request.method == 'GET':
        return signup_get(request)
    elif request.method == 'POST':
        return signup_post(request)

def signin(request):
    if request.method == 'GET':
        return signin_get(request)
    elif request.method == 'POST':
        return signin_post(request)

def password_modify(request):
    if request.method == 'GET':
        return password_modify_get(request)
    elif request.method == 'POST':
        return password_modify_post(request)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('calender:show')

def withdraw(request):
    if request.method == 'GET':
        return withdraw_get(request)
    elif request.method == 'POST':
        return withdraw_post(request)

# view function

def signup_get(request):
    signupForm = SignupForm()
    return render(request, 'user/signup.html', {'form' : signupForm})

def signup_post(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        try:
            form.save()
        except forms.ValidationError:
            return render(request, 'error.html', {'errorReason' : "Exist User ID"})
    return redirect('signin')

def signin_get(request):
    signinForm = SigninForm()
    return render(request, 'user/signin.html', {'form' : signinForm})

def signin_post(request):
    form = SigninForm(request.POST)
    if form.is_valid():
        user_id = form.signin()
        request.session['user_id'] = user_id
    return redirect('/calender/show')

def password_modify_get(request):
    passwordModifyForm = PasswordModifyForm()
    return render(request, 'user/password_modify.html', {'form' : passwordModifyForm})

def password_modify_post(request):
    return redirect('calender:show')

def withdraw_get(request):
    withdrawForm = WithdrawForm()
    return render(request, 'user/withdraw.html', {'form' : withdrawForm})

def withdraw_post(reuqest):
    return redirect('signin')
