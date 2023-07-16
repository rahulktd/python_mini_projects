from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.forms import StudentForm
from core.models import Notification


# Create your views here.
def index(request):
    return render(request,'Modified_files/index.html')

def admin_dashboard(request):
    return render(request,"Admin/Admin_dash.html")

def student_dashboard(request):
    student = request.user
    notifications = Notification.objects.filter(student=student).order_by('-created_at')
    return render(request,"Student/USER_DASH.html",{'notifications': notifications})

def signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request,'Modified_files/sign_up.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'Modified_files/login.html')

def logout_view(request):
    logout(request)
    return redirect('loginview')


