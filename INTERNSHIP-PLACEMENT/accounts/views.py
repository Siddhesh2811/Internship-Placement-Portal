from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import studentUser, companyUser
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django_email_verification import send_email


# Create your views here.


def index(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'index.html', {'suser': suser, 'cuser': cuser})


def stusignup(request):
    if request.method == 'POST':
        yourname = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        email = request.POST['email']
        branch = request.POST['branch']
        yog = request.POST['yog']
        contact = request.POST['contact']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                mess = "Username is already taken."
                return render(request, 'stusignup.html', {'mess': mess})
            elif User.objects.filter(email=email).exists():
                mess = "Email is already taken."
                return render(request, 'stusignup.html', {'mess': mess})
            else:
                user = User.objects.create_user(email=email,
                                                username=username, password=password1)
                user.is_active = False  # Example
                send_email(user)
                suser = studentUser(username=username, yourname=yourname,
                                    email=email, yog=yog, contact=contact, branch=branch, user=user)
                # Example
                suser.save()
                mess1 = "Please check your mail inbox to verify your account."
                return render(request, 'stusignin.html', {'mess1': mess1})
        else:
            mess = "Password is incorrect."
            return render(request, 'stusignup.html', {'mess': mess})
    else:
        return render(request, 'stusignup.html')


def checkstu(username):
    suser = studentUser.objects.all()
    for u in suser:
        if username == u.username:
            return True
    return False


def checkcom(username):
    cuser = companyUser.objects.all()
    for u in cuser:
        if username == u.username:
            return True
    return False


def stusignin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if checkstu(username):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard')
            else:
                mess = "Invalid Credentials."
                return render(request, 'stusignin.html', {'mess': mess})
        else:
            mess = "Invalid Credentials."
            return render(request, 'stusignin.html', {'mess': mess})
    else:
        return render(request, 'stusignin.html')


def comsignin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if checkcom(username):
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard/comdashboard')
            else:
                mess = "Invalid Credentials."
                return render(request, 'comsignin.html', {'mess': mess})
        else:
            mess = "Invalid Credentials."
            return render(request, 'comsignin.html', {'mess': mess})
    else:
        return render(request, 'comsignin.html')


def comsignup(request):
    if request.method == 'POST':
        companyname = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['pass']
        password2 = request.POST['re_pass']
        companyemail = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                mess = "Username is already taken."
                return render(request, 'comsignup.html', {'mess': mess})
            elif User.objects.filter(email=companyemail).exists():
                mess = "Email is already taken."
                return render(request, 'comsignup.html', {'mess': mess})
            else:
                user = User.objects.create_user(email=companyemail,
                                                username=username, password=password1)
                cuser = companyUser(username=username, companyname=companyname,
                                    companyemail=companyemail, contact=contact, address=address, user=user)
                cuser.save()
                return redirect('/comsignin')
        else:
            mess = "Password is incorrect."
            return render(request, 'comsignup.html', {'mess': mess})
    else:
        return render(request, 'comsignup.html')


def aboutus(request):
    suser = studentUser.objects.all()
    cuser = companyUser.objects.all()
    return render(request, 'aboutus.html', {'suser': suser, 'cuser': cuser})


def logout(request):
    auth.logout(request)
    return redirect('/')
