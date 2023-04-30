from django .urls import path
from . views import *

urlpatterns = [
    path('', Home),
    path('login', Login, name='login'),
    path('signup', Signup, name='signup'),
    path('student', Student, name='student'),
    path('teacher', Teacher, name='teacher'),
    path('staff', Staff, name='staff'),
    path('student_out', StudentLogout, name='student_out'),
    path('teacher_out', TeacherLogout, name='teacher_out'),
    path('staff_out', StaffLogout, name='staff_out'),
]