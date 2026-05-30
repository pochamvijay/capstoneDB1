from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from app.models import Employee


def login(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:

            auth_login(request,user)

            return redirect('/home/')

        else:

            error = "Wrong Username or Password"

    return render(request,'app/login.html',{'error':error})


def register(request):

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        User.objects.create_user(

            username=username,
            email=email,
            password=password

        )

        return redirect('/')

    return render(request,'app/register.html')


def home(request):

    employees = Employee.objects.all()

    return render(request,'app/home.html',{'employees':employees})


def add_employee(request):

    if request.method == "POST":

        fullname = request.POST['fullname']
        designation = request.POST['designation']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        image = request.POST['image']

        Employee.objects.create(

            fullname=fullname,
            designation=designation,
            phone=phone,
            email=email,
            address=address,
            image=image

        )

        return redirect('/home/')

    return render(request,'app/add_employee.html')


def detail(request,id):

    employee = Employee.objects.get(id=id)

    return render(request,'app/employee_detail.html',{'employee':employee})


def logout(request):

    auth_logout(request)

    return redirect('/')