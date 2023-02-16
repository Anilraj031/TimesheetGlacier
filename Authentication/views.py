from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from .models import LoggedUser,Company,Employees
from Manager.models import InitialPassword
import re
from django.contrib.auth.hashers import check_password
from Attendance.models import LeaveType
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid:
            fm.save()
        else:
            fm = UserCreationForm()
            messages.success(request, 'Somethings Wrong! Please try again with different value')
            
    else:
        fm = UserCreationForm()
    return render(request, 'Authentication/register.html', {'form':fm})


def login_n(request):
    if not request.user.is_authenticated :
        if request.method == 'POST':
            uname = request.POST['username']
            upass = request.POST['password']
            user = authenticate(username=uname, password=upass)
            #print(upass)
            if user is not None:
                login(request,user)
                LoggedUser(user=request.user).save()
                #print(request.user.id)
                
                if request.user.is_authenticated:
                    createSession(request)
                    checkPassword = InitialPassword.objects.get(user=request.user.id)
                    if checkPassword.first_changed == False:
                        return HttpResponseRedirect(reverse('newPassword'))
                    else:
                        return HttpResponseRedirect(reverse('home'))
            
        else:
            fm = AuthenticationForm()
        fm = AuthenticationForm()
        return render(request, 'Authentication/login.html', {'form':fm})
    else:
        checkPassword = InitialPassword.objects.get(user=request.user.id)
        if checkPassword.first_changed == False:
            return HttpResponseRedirect(reverse('newPassword'))
        else:
            return HttpResponseRedirect(reverse('home'))

def logout_n(request):
    LoggedUser.objects.filter(user=request.user).delete()
    logout(request)
    return HttpResponseRedirect('login')

def getUser(request):
    if request.user.is_authenticated :
        username = str(request.user)
        return JsonResponse({'user':username})
    else:
        return HttpResponseRedirect('login')

def changePassword(request):
    return render(request, "Authentication/newPassword.html")

def updatePassword(request):
    if request.method == 'POST':
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        check = checkPassword(request,pass2)
        print()
        
        if(pass1 != pass2 ):
            return JsonResponse({'result':"Password didn't matched!"})
        elif(check != 'Success' ):
            return JsonResponse({'result':check})
        else:
            usr = User.objects.get(username=request.user.username)
            usr.set_password(pass1)
            usr.save()
            InitialPassword.objects.filter(user_id=request.user.id).update(first_changed=True)
            return JsonResponse({'result':"Success"})
            #return HttpResponseRedirect(reverse('home'))

def resetPassword(request):
    return render(request, "Authentication/ResetPassword.html")


def checkPassword(request,password):
    password = password
    flag = ''
    currentpassword = request.user.password
    matchcheck= check_password(password, currentpassword)
    while True:
        if (len(password)<=8):
            flag = 'Password must contain 8 characters!'
            break
        elif not re.search("[a-z]", password):
            flag = 'Password must contain [a-z] characters!'
            break
        elif not re.search("[0-9]", password):
            flag = 'Password must contain numbers[0-9] characters!'
            break
        elif not re.search("[_@$!]" , password):
            flag = 'Password must contain one special characters!'
            break
        elif matchcheck:
            flag = 'Please enter new password!'
            break
        else:
            flag = 'Success'
            break
    return flag


def userSetting(request):
    ltypes = LeaveType.objects.all()
    return render(request,'Authentication/usersettings.html',{'ltypes':ltypes})

def createSession(request):
    companyid = Employees.objects.get(user=request.user)
    #print(companyid.company.name)
    request.session['company'] =companyid.company.name
    return True
@csrf_exempt
def activateUser(request):
    id=request.POST.get('userid')
    action = request.POST.get('action')
    if action=="true":
        User.objects.filter(id=id).update(is_active=True)
        return JsonResponse({'result':"Success"})
    else:
        User.objects.filter(id=id).update(is_active=False)
        return JsonResponse({'result':"Success"})


@csrf_exempt
def adminUser(request):
    id=request.POST.get('userid')
    action = request.POST.get('action')
    if action=="true":
        User.objects.filter(id=id).update(is_superuser=True)
        return JsonResponse({'result':"Success"})
    else:
        User.objects.filter(id=id).update(is_superuser=False)
        return JsonResponse({'result':"Success"})


