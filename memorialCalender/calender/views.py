from django.shortcuts import render
from .models import Calender, User

def show_calender(request):
    user = User.objects.filter(user_id=request.session['user_id']).first()
    calender = Calender.objects.filter(user_id=user).all()
    return render(request, 'calender/show.html', {'user_id' : request.session['user_id'], 'calender' : calender})

def set_calender(request):
    pass