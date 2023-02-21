from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import worklog,tasktype
from Project.models import Project, SubProject
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, date
from django.http import JsonResponse


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

def dailylog(request):
    all_data=worklog.objects.all().order_by('-Date')
    task =tasktype.objects.all().values()

    # This is for search
    if request.method=="GET":
        username=request.GET.get('searching')
        if username!=None:
            all_data=worklog.objects.filter(User__icontains=username)

    # paginatio
    paginator=Paginator(all_data,10)
    page_number=request.GET.get('page')
    page_datafinal=paginator.get_page(page_number)
    totalpage=page_datafinal.paginator.num_pages

    # print(all_data)
    context= {
        'all_data':all_data, 
        'tasktype':task,

        # pagination
        'all_data':page_datafinal,
        'totalpage':[n+1 for n in range(totalpage)]
    }
    #print(context)
    return render(request, 'dailylog.html', context)

# This is for adding record
def ADD(request):
    if request.method == "POST":
        date =request.POST.get('date')
        tasktype =request.POST.get('tasktype')
        task_id = request.POST.get('subproject')
        workdone =request.POST.get('workdone')
        hours =int(request.POST.get('hours'))
        billable =request.POST.get('billable')
        action = request.POST.get('action')
        id=request.POST.get('id')

        if billable == 'on': 
            b1=True 
        else:
            b1=False
        if action == 'update':
            worklog.objects.filter(id=id).update(Date=date,TaskType_id=tasktype,Workdone=workdone,Hours=hours,Billable=b1)
        else:
            datas = worklog (
                User = request.user ,
                Date = date,
                TaskType_id = tasktype,
                project_id = SubProject.objects.get(id=task_id),
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

    # context= {
    #     'all_data':all_data,
    # }
    return redirect('dailylog')

def gets(request):        
    data=Project.objects.all().values()
    return JsonResponse({'result':list(data)})

def subproject(request):
    id=request.GET['id']
    subdata=SubProject.objects.filter(project=id).values()
    # print(request.user)
    return JsonResponse({'result':list(subdata)})
