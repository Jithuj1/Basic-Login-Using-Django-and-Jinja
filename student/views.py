from django.shortcuts import render, redirect
from .models import User


def Home(request):
    return render(request, 'home/home.html')

def Signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        role = request.POST.get('role')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name == '' or phone == '' or role == '' or country == '' or email == '' or password == '':
            error = {'message' : 'blank space is not allowed'}
            return render(request, 'home/signup.html', error)
        elif User.objects.filter(email=email).exists():
            error = {'message' : 'Email already taken'}
            return render(request, 'home/signup.html', error)
        elif len(password)<5 :
            error = {'message' : 'password need min 5 letter'}
            return render(request, 'home/signup.html', error)
        else:
            obj = User()
            obj.name = name
            obj.phone = phone
            obj.country = country
            obj.role = role
            obj.email = email
            obj.password = password
            obj.save()
            return render(request, 'home/login.html')
    else:
        return render(request, 'home/signup.html')

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pword = request.POST.get('password')
        if email == '' or pword == '':
            msg = {'message':'Blank space is not allowed'}
            return render(request, 'home/login.html', msg)
        elif len(pword)<5:
            msg = {'message': 'Password must have at least 5 letter'}
            return render(request, 'home/login.html', msg)
        try:
            user = User.objects.get(email=email, password=pword)
            if user:
                if user.role == 'student':
                    request.session['student'] = email
                    return redirect('student')
                elif user.role == 'teacher':
                    request.session['teacher'] = email
                    return redirect('teacher')
                else:
                    request.session['staff'] = email
                    return redirect('staff')
        except:
            msg = {'msg': 'wrong password'}
            return render(request, 'home/login.html', msg)
    else:
        return render(request, 'home/login.html')
    

def Student(request):
    if 'student' in request.session:
        return render(request, 'student.html')
    else:
        return redirect('login')
    

def Teacher(request):
    if 'teacher' in request.session:
        return render(request, 'teacher.html')
    else:
        return redirect('login')


def Staff(request):
    if 'staff' in request.session:
        return render(request, 'staff.html')
    else:
        return redirect('login')
    
def StudentLogout(request):
    if 'student' in request.session:
        del request.session['student']
    return redirect('/')

def TeacherLogout(request):
    if 'teacher' in request.session:
        del request.session['teacher']
    return redirect('/')

def StaffLogout(request):
    if 'staff' in request.session:
        del request.session['staff']
    return redirect('/')