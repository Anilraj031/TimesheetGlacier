from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import worklog,tasktype
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, date


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

# This is for filter
# def filter(request):
#     all_data=worklog.objects.all().order_by('-Date')

#     if request.method=="GET":
#         username=request.GET.get('searching')
#         if username!=None:
#             all_data=worklog.objects.filter(User__icontains=username)


#     context= {
#         'all_data':all_data
#     }
#     return render(request, 'dailylog.html', context)

# This is for using read data form database
def dailylog(request):
    all_data=worklog.objects.all().order_by('-Date')
    task =tasktype.objects.all().values()

    # This is for search
    if request.method=="GET":
        username=request.GET.get('searching')
        if username!=None:
            all_data=worklog.objects.filter(User__icontains=username)

    # paginatio
    paginator=Paginator(all_data,5)
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
        user =request.POST.get('user')
        date =request.POST.get('date')
        tasktype =request.POST.get('tasktype')
        workdone =request.POST.get('workdone')
        hours =int(request.POST.get('hours'))
        billable =request.POST.get('billable')

        if billable == 'on': 
            b1=True 
        else:
            b1=False
        datas = worklog (
            User = request.user ,
            Date = date,
            TaskType_id = tasktype,
            Workdone = workdone,
            Hours = hours,
            Billable = b1
        )
        datas.save()
        return redirect('dailylog')

    # all_data=worklog.objects.all()
    # task =tasktype.objects.all().values()    
    # context= {
    #     'all_data':all_data,
    #     'tasktype':task
    # }
    # return render(request, 'test1.html')

# This is for editing record
def Edit(request):
    all_data=worklog.objects.all()
    context= {
        'all_data':all_data,      
    }
    return redirect(request, 'dailylog.html', context)

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


