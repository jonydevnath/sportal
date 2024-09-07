from django.shortcuts import render, redirect
from .models import Enroll, Notice, Routine
from .forms import EnrollForm, NoticeForm, RoutineForm

# Create your views here.
def home(request):
    enrolls = Enroll.objects.all()
    notices = Notice.objects.all()
    routines = Routine.objects.all()
    return render(request, 'home.html', {'enrolls': enrolls, 'notices': notices, 'routines': routines})

def enroll(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = EnrollForm()
    return render(request, 'enroll.html', {'form': form})

def notice(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = NoticeForm()
    return render(request, 'notice.html', {'form': form})

def enrollment(request):
    return render(request, "enrollment.html", {})

def homeworks(request):
    return render(request, "homeworks.html", {})

def login(request):
    return render(request, "login.html", {})

def routine(request):
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after saving
    else:
        form = RoutineForm()
    return render(request, 'routine.html', {'form': form})

