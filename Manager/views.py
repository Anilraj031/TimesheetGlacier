from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User,Permission
from .models import InitialPassword
from django.views.decorators.csrf import csrf_exempt
from Authentication.models import Company
from Attendance.models import Attendance,Leave,TrackAttendance
from datetime import date,datetime
import numpy as np
import re
from emp_worklog.models import worklog
from django.db.models import Sum
from Project.models import Project

# Create your views here.
def getDetails(request):
    allusers =User.objects.all().values('id','username')
    data = {
            'users' :allusers
        }
    return render(request, 'Reports/user_reports.html',data)

@csrf_exempt
def getusers(request):
    if request.method == 'POST':
        status = request.POST['status']
        if status == '1': #active
            allusers = User.objects.filter(is_active=True)
        elif status == '2':
            allusers = User.objects.filter(is_active=False)
        else:
            allusers = User.objects.all()
        
        data = []
        for x in allusers:
            data.append({
                'id':x.id,
                'username':x.username,
                'email':x.email,
                'firstname':x.first_name,
                'lastname':x.last_name,
                'active':x.is_active
            })
        return JsonResponse({'result':data})
    else:
        allusers = User.objects.filter(is_active=True)
        data = {
                'users' :allusers
            }
        #print(data)
        return render(request,'Reports/users.html',data)

def newUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        n_email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        action = request.POST.get('action')
        userId = request.POST.get('id')
        usr = User.objects.filter(username=username).count()
        #print(id)
        if(action == 'create'):
            check = checkPassword(request, pass2)
            if pass1 != pass2:
                return JsonResponse({'result':"Password didn't match"})
            elif usr != 0 and action == 'create':
                return JsonResponse({'result':"Username alredy exists"})
            elif check != 'Success':
                return JsonResponse({'result':check})
            else:
                newUser = User.objects.create(username=username,email=n_email,password=pass1)
                #newUser.first_name=fname
                #newUser.last_name =lname
                newUser.save()
                new_user = User.objects.get(username=username)
                #print(new_user.id)
                newP=InitialPassword(user=new_user,first_password=pass1,first_changed=False)
                newP.save()
                attendanceTrack = TrackAttendance(user=new_user,btn1=False,btn2=False,btn3=True)
                attendanceTrack.save()
                return JsonResponse({'result':"Success"})
        elif(action == 'update'):
            User.objects.filter(id=userId).update(username=username,first_name=fname,last_name=lname,email=n_email)
            return JsonResponse({'result':"Successfully Updated"})
    else:
        return render(request,'Reports/users.html')

def updateUser(request,userId):
    getUser = User.objects.get(id=userId)
    data = {
        'users':getUser
    }
    return render(request,'Reports/updateUser.html',data)

def viewUser(request,userId):
    getUser = User.objects.get(id=userId)
    perm = Permission.objects.filter(user=getUser)

    #user work details
    issue = worklog.objects.filter(User=getUser,TaskType=1).count()
    totalIssue = worklog.objects.filter(TaskType=1).count()
    totalProject = worklog.objects.filter(User=getUser,TaskType=2)
    project = Project.objects.filter(manager=getUser)

    hour = worklog.objects.filter(Billable=True).aggregate(Sum('Hours'))
    totalhour = Attendance.objects.filter(user=getUser).aggregate(Sum('hour'))
    
    leave = Leave.objects.filter(user=getUser).count()
    attendance = Attendance.objects.filter(user=getUser).count()
    details = {
        'issue':issue,
        'totalIssue':totalIssue,
        'project':project.count(),
        'totalProject':totalProject.count(),
        'hour':hour,
        'totalHour':totalhour,
        'leave':leave,
        'attendance':attendance
    }
    pid = []
    for x in perm:
        pid.append(x.id)
    #print(pid)
    #projects details
    #print(project)
    data = {
        'users':getUser,
        'permissions':pid,
        'summary':details,
        'projects':project,
        'hours':totalProject
    }
    #print(getUser.last_name)
    return render(request,'Reports/userDetails.html',data)

@csrf_exempt
def addPermissions(request):
    userid = request.POST.get('user')
    permissionId = request.POST.get('pid')
    actn = request.POST.get('action')
    nUser = User.objects.get(id=userid)
    np = Permission.objects.get(id=permissionId)
    if actn == 'add':
        nUser.user_permissions.add(np)
    else:
        nUser.user_permissions.remove(np)
    return JsonResponse({'result':"Success"})


def company(request):
    comp = Company.objects.get(id=1)
    return render(request,'Reports/company.html',{'company':comp})

@csrf_exempt
def report(request):
    user_id = request.POST['user']
    date1 = request.POST['from']
    date2 = request.POST['to']
    user_details = {}
    #print(user_id)
    if user_id != '0':
        user = User.objects.get(id=user_id)
        user_details = {
            'name':user.username,
            'fname':user.first_name,
            'lname':user.last_name,
            'email':user.email,
            'joined':user.date_joined.date(),
            'login':user.last_login.date()
        }

    attendance = Attendance.objects.filter(user=user_id,date__range=(date1,date2)).values()
    leave  = Leave.objects.filter(user=user_id,date__range=(date1,date2)).values()
    days = np.busday_count(date1, date2)
    l_taken =  Leave.objects.filter(user=user_id,date__range=(date1,date2),approval=1).count()
    total = attendance.count()
    a_details = {
        'worked':str(total),
        'total':str(days),
        'leave':str(l_taken)
    }
    #new_data = attendance.union(leave)
    #print(a_details)
    data={
        'user':user_details,
        'attendance':list(attendance),
        'leave':list(leave),
        'atdnc':a_details
    }
    #print(attendance)
    return JsonResponse(data)

def checkPassword(request,password):
    password = password
    flag = ''
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
        else:
            flag = 'Success'
            break
    return flag
