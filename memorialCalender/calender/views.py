from django.shortcuts import render

def show_calender(request):
    return render(request, 'calender/show.html')

def set_calender(request):
    pass