from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import worklog,tasktype
from Project.models import Project, SubProject
from Issue.models import Ticket
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Q
from dateutil.relativedelta import relativedelta,MO
from django.db.models import Sum
from django.contrib.auth.models import User
from Customer.models import customer
<<<<<<< HEAD
from Manager.views import checkTeams
from django.views.decorators.csrf import csrf_exempt


=======
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
# Create your views here.
def dailylog1(request):
    all_data=worklog.objects.all()
    context= {
        'all_data':all_data
    }
    print(context)
    return render(request, 'dailylog1.html', context)

def billable(request):
    return render(request, 'billable.html')

def nonbillable(request):
    return render(request, 'non_billable.html')

def index(request):
    return render(request, 'index.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def test(request):
    return render(request, 'test.html')

def enterrecord(request):
    return render(request, 'enterrecordform.html')

def addrecord(request):
    return render(request, 'addrecord.html')

<<<<<<< HEAD
@csrf_exempt
def dailylog(request):
    #view list of users if users is admin or team leader
    getTeam_users = checkTeams(request)
    allusers = User.objects.filter(pk__in=getTeam_users[0])
    
=======
def dailylog(request):
    all_data=worklog.objects.filter(User = request.user)
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
    task =tasktype.objects.all().values()

    date = datetime.today().weekday()
    if date == 0: #0=monday
        today = datetime.today()#-timedelta(days=1)#datetime.today()
    else:
        today = datetime.today()
    lastMonday = today + relativedelta(weekday=MO(-1))
    nextMonday = today + relativedelta(weekday=MO(1))
    
<<<<<<< HEAD
    
    all_data=worklog.objects.filter(User = request.user,Date__month=today.month)
    # pagination
=======
    thisweekdata = worklog.objects.filter(User = request.user,Date__range=(lastMonday,nextMonday))
    #print(weekdata)
    #for last weeks log
    lastMonday2 = today + relativedelta(weekday=MO(-2))
    lastweekdata = worklog.objects.filter(User = request.user,Date__range=(lastMonday2,lastMonday-timedelta(days=1)))
    
    allusers =User.objects.all().values('id','username')
    # This is for search
    if request.method=="GET":
        username=request.GET.get('searching')
        if username!=None:
            all_data=worklog.objects.filter(User__icontains=username)

    # paginatio
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
    paginator=Paginator(all_data,10)
    page_number=request.GET.get('page')
    page_datafinal=paginator.get_page(page_number)
    totalpage=page_datafinal.paginator.num_pages

<<<<<<< HEAD
    if request.method == 'POST':
        user = request.POST.get('id')
        thisweekdata = worklog.objects.filter(User = user,Date__range=(lastMonday,nextMonday))
        #for last weeks log
        lastMonday2 = today + relativedelta(weekday=MO(-2))
        lastweekdata = worklog.objects.filter(User = user,Date__range=(lastMonday2,lastMonday-timedelta(days=1)))
        context= {
            'all_data':list(all_data.values()), 
            'tasktype':list(task),
            'lastweekdata':get_Projectnames(request,lastweekdata),
            'lastweektotal':lastweekdata.aggregate(Sum('Hours')),
            'thisweekdata':get_Projectnames(request,thisweekdata),
            'thisweektotal':thisweekdata.aggregate(Sum('Hours')),
            
        }

        return JsonResponse({'result':context})
    
    if request.method == 'GET':
        thisweekdata = worklog.objects.filter(User = request.user,Date__range=(lastMonday,nextMonday))
        #for last weeks log
        lastMonday2 = today + relativedelta(weekday=MO(-2))
        lastweekdata = worklog.objects.filter(User = request.user,Date__range=(lastMonday2,lastMonday-timedelta(days=1)))
        context= {
            'all_data':all_data, 
            'tasktype':task,
            'lastweekdata':lastweekdata,
            'lastweektotal':lastweekdata.aggregate(Sum('Hours')),
            'thisweekdata':thisweekdata,
            'thisweektotal':thisweekdata.aggregate(Sum('Hours')),
            'is_team':getTeam_users[1],
            # pagination
            'all_data':page_datafinal,
            'totalpage':[n+1 for n in range(totalpage)],
            'users':allusers
        }
        return render(request, 'dailylog.html', context)
        
#jquery filed name display
def get_Projectnames(request,result):
    #print(result[1].Date)
    data = []
    for d in result:
        data.append({
            'date':''+d.Date.strftime("%B %d, %Y"),
            'project': get_project_or_task_empty(request,d.project_id_id,'project'),
            'tasktype':get_project_or_task_empty(request,d.TaskType.id,'tasktype'),
            'task':get_project_or_task_empty(request,d.task_id,'task'),
            'priority': get_project_or_task_empty(request,d.task_id,'priority'),
            'hours':d.Hours,
            'billable':d.Billable,
            'id':d.id
        })
    #print(data)
    return data

def get_project_or_task_empty(request,id,type):
    #print(id)
    name = 'none'
    if type =='tasktype':
        if id != None:
            name1 = tasktype.objects.get(id=id)
            name = name1.TaskType
    elif type == 'project':
        if id != None:
            name1 = SubProject.objects.get(id=id)
            name=name1.name
    elif type =='task':
         if id != None:
            name1 = Ticket.objects.get(id=id)
            name=name1.ticket_name
    else:
        if id != None:
            name1 = Ticket.objects.get(id=id)
            name=name1.priority
    return name
=======
    context= {
        'all_data':all_data, 
        'tasktype':task,
        'lastweekdata':lastweekdata,
        'lastweektotal':lastweekdata.aggregate(Sum('Hours')),
        'thisweekdata':thisweekdata,
        'thisweektotal':thisweekdata.aggregate(Sum('Hours')),

        # pagination
        'all_data':page_datafinal,
        'totalpage':[n+1 for n in range(totalpage)],
        'users':allusers
    }
    #print(context)
    return render(request, 'dailylog.html', context)
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06

# This is for adding record
def ADD(request):
    if request.method == "POST":
        date =request.POST.get('date')
        tasktype =request.POST.get('tasktype')
        project_id = request.POST.get('sublist')
        task_id = request.POST.get('issue_list')
        workdone =request.POST.get('workdone')
        hours =int(request.POST.get('hours'))
        billable =request.POST.get('billable')
        action = request.POST.get('action')
        id=request.POST.get('id')

        if billable == 'on': 
            b1=True 
        else:
            b1=False
        print(project_id)
        if project_id != None:
            project = SubProject.objects.get(id=project_id)
        else:
            project = None

        if task_id != None:
            task = Ticket.objects.get(id=task_id)
        else:
            task = None
        
        if action == 'update':
            worklog.objects.filter(id=id).update(Date=date,TaskType_id=tasktype,project_id=project,task=task,Workdone=workdone,Hours=hours,Billable=b1)
        else:
            datas = worklog (
                User = request.user ,
                Date = date,
                TaskType_id = tasktype,
                project_id = project,
                task = task,
                Workdone = workdone,
                Hours = hours,
                Billable = b1
            )
            datas.save()
        return redirect('dailylog')

# This is for editing record
def Edit(request):
    logId = request.GET.get('id')
    data=worklog.objects.filter(id=logId).values()

    return JsonResponse({'result':list(data)})

# This is for updating record
def Update(request,id):
    if request.method == "POST":
        user=request.POST.get('user')
        date=request.POST.get('date')
        tasktype=request.POST.get('tasktype')
        workdone=request.POST.get('workdone')
        hours=int(request.POST.get('hours'))
        billable=request.POST.get('billable')

        if billable == 'on': 
            b1=True 
        else:
            b1=False

        datas = worklog (
            id = id,
            User = user,
            Date = date,
            TaskType_id = tasktype,
            Workdone = workdone,
            Hours = hours,
            Billable = b1
        )
        datas.save()
        return redirect('dailylog')
    return redirect(request,'dailylog.html')

# This is for deleting record
def Delete(request,id):
    all_data=worklog.objects.filter(id = id)
    all_data.delete()
    return redirect('dailylog')

def gets(request):   
    task_id=request.GET.get('task')
    #print(task_id)   
    if task_id == '1':
        data=Ticket.objects.filter(Q(state='New')| Q(state='InProgress')).values()
    elif task_id == '2':
        data=Project.objects.all().values()
    else:
        data=""
    return JsonResponse({'result':list(data)})

def subproject(request):
    id=request.GET['id']
    subdata=SubProject.objects.filter(project=id).values()
    # print(request.user)
    return JsonResponse({'result':list(subdata)})


def getMonthlyHours(request):
    year = datetime.today().year
    month = datetime.today().month
    
<<<<<<< HEAD
=======

>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
    data = {}
    keys = range(1,13)
    for i in keys:
        data[i] = worklog.objects.filter(Date__year =year,Date__month= i,Billable=True).aggregate(Sum('Hours'))

    result={
        'year':year,
        'test':data
    }
    return JsonResponse(result)


def getHoursData(request):
    gethour = customer.objects.all().aggregate(Sum('contract_hr')).get('contract_hr__sum', 0.00)
    users = User.objects.all()
    usr_hour = []
    for x in users:
        usr_hour.append({
            'user':x.username,
            'hour':worklog.objects.filter(Date__month=datetime.today().month,User = x.id).aggregate(Sum('Hours')).get('Hours__sum', 0.00)
        })
    
    achievedhr = worklog.objects.filter(Date__month=datetime.today().month,Billable=True).aggregate(Sum('Hours')).get('Hours__sum', 0.00)
<<<<<<< HEAD
    return JsonResponse({'requiredHr':gethour,'users':usr_hour,'hour':achievedhr})


@csrf_exempt
def getLogByUsers(request):
    if request.method =='POST':
        u_id = request.POST.get('id')

    return JsonResponse({'result':'success'})
=======
    return JsonResponse({'requiredHr':gethour,'users':usr_hour,'hour':achievedhr})
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
