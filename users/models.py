from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User Model (Roles: Admin, Teacher, Student, Parent)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'}, related_name='courses_taught'
    )

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        ordering = ['name']


# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    courses = models.ManyToManyField(Course, related_name='enrolled_students')

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']


# Parent Model (Optional)
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    children = models.ManyToManyField(Student, related_name='parents')

    def __str__(self):
        return self.user.username


# Attendance Model
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)  # True for Present, False for Absent

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} ({'Present' if self.status else 'Absent'})"

    class Meta:
        ordering = ['-date']
        unique_together = ('student', 'course', 'date')  # Ensures one attendance record per student per day
