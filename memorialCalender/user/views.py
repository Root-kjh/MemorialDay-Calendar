from django.shortcuts import render, redirect

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
    return render(request, 'user/signup.html')

def signup_post(request):

    return redirect('user:signin', 'signin')

def signin_get(request):
    return render(request, 'user/signin.html')

def signin_post(request):
    return redirect('calender:show')

def password_modify_get(request):
    return render(request, 'user/password_modify.html')

def password_modify_post(request):
    return redirect('calender:show')

def withdraw_get(request):
    return render(request, 'user/withdraw.html')

def withdraw_post(reuqest):
    return redirect('user:signin')
