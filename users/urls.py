from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register, profile, admin_dashboard, students_list, courses_list, attendance_list,logout_view,teacher_dashboard, student_dashboard, parent_dashboard

urlpatterns = [
    path('', home, name='home'),  #done
    path('register/', register, name='register'), #done
    path('profile/', profile, name='profile'),  #done
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #done
    path('logout/', logout_view, name='logout'),  #done
     path('dashboard/', admin_dashboard, name='dashboard'), #done
    path('students/', students_list, name='students_list'), #done
    path('courses/', courses_list, name='courses_list'), #done
    path('attendance/', attendance_list, name='attendance_list'),
    path('dashboard/teacher/', teacher_dashboard, name='teacher_dashboard'), #done
    path('dashboard/student/', student_dashboard, name='student_dashboard'), #done
    path('dashboard/parent/', parent_dashboard, name='parent_dashboard'), #done
]

