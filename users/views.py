from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserUpdateForm
from .models import Student, Course, Attendance
from .decorators import role_required

# 🔹 User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = CustomUserCreationForm()  # Fixed form reference

    return render(request, 'register.html', {'form': form})

# 🔹 User Profile
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Stay on profile page after update
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})

# 🔹 Dashboard for Admin
@login_required
@role_required(['admin'])
def admin_dashboard(request):
    context = {
        'students': Student.objects.all(),
        'courses': Course.objects.all(),
        'attendance_records': Attendance.objects.all()
    }
    return render(request, 'dashboard.html', context)

# 🔹 List Views (Students, Courses, Attendance)
@login_required
def students_list(request):
    return render(request, 'students_list.html', {'students': Student.objects.all()})

@login_required
def courses_list(request):
    return render(request, 'courses_list.html', {'courses': Course.objects.all()})

@login_required
def attendance_list(request):
    return render(request, 'attendance_list.html', {'attendance_records': Attendance.objects.all()})

# 🔹 Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# 🔹 Role-Based Dashboards
@login_required
@role_required(['teacher'])
def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

@login_required
@role_required(['student'])
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

@login_required
@role_required(['parent'])
def parent_dashboard(request):
    return render(request, 'parent_dashboard.html')

# 🔹 Homepage
def home(request):
    return render(request, 'home.html')
