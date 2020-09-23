from django.shortcuts import render, redirect

def index(request):
    if request.session.get('user'):
        return redirect('/calender/show')
    else:
        return render(request, 'index/index.html')