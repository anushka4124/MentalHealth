
from django.shortcuts import render, get_object_or_404, redirect
from .models import Resource, Therapist, Appointment, ForumPost
from support.form import AppointmentForm
from django.contrib.auth.decorators import login_required

def index(request):
    resources = Resource.objects.all()
    return render(request, 'index.html', {'resources': resources})

def therapist_list(request):
    therapists = Therapist.objects.all()
    return render(request,'therapist_list.html', {'therapists': therapists})

def forum(request):
    posts = ForumPost.objects.all()
    return render(request, 'forum.html', {'posts': posts})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointments')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

@login_required
def appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments.html', {'appointments': appointments})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .acc_form import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})