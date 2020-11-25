from django.shortcuts import redirect

def index(request):
    if request.session.get('user'):
        return redirect('/calender/show')
    else:
        return redirect('/user/signin')