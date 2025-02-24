from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .models import User,Student, Course, Attendance
from .forms import CustomUserCreationForm
from .decorators import role_required

# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# User Profile
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
@role_required(['admin'])
def admin_dashboard(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    attendance_records = Attendance.objects.all()
    return render(request, 'dashboard.html', {
        'students': students,
        'courses': courses,
        'attendance_records': attendance_records
    })

@login_required
def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})

@login_required
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses_list.html', {'courses': courses})
@login_required
def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance_records': attendance_records})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

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

def home(request):
    return render(request, 'home.html')