from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register, profile, admin_dashboard, students_list, courses_list, attendance_list,logout_view,teacher_dashboard, student_dashboard, parent_dashboard

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),  # Logout URL
     path('dashboard/', admin_dashboard, name='dashboard'),
    path('students/', students_list, name='students_list'),
    path('courses/', courses_list, name='courses_list'),
    path('attendance/', attendance_list, name='attendance_list'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/student/', student_dashboard, name='student_dashboard'),
    path('dashboard/parent/', parent_dashboard, name='parent_dashboard'),
]

