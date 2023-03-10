from django.shortcuts import render
from django.shortcuts import redirect
from . models import Ticket
from Attendance.models import User
from Customer.models import employee

# Create your views here.
# function based views
def index(request):
    allusers =User.objects.all().values('id','username')
    ticket = Ticket.objects.all()
    customer = employee.objects.all().values()
    #print(customer)
    dic = {
        'ticket':ticket,
        'users':list(allusers),
        'customer':list(customer)
        }
    return render(request, 'Issues/allIssues.html', dic)

def getIssue(request,issueid):
    issue = Ticket.objects.get(id=issueid)
    allusers =User.objects.all().values('id','username')
    customer = employee.objects.all().values()
    #print(allusers)
    return render(request, 'Issues/details.html',{'issue':issue,'users':allusers,'customer':customer})

def ADD(request):
    if request.method == "POST":
        ticketName = request.POST.get('ticketName')
        ticketType = request.POST.get('ticketType')
        shortDesc = request.POST.get('shortDesc')
        dateOpened = request.POST.get('dateOpened')
        affUser = request.POST.get('affUser')
        priority = request.POST.get('priority')
        state = request.POST.get('state')
        assGroup = request.POST.get('assGroup')
        assTo = request.POST.get('assTo')
        email = request.POST.get('email')
        comments = request.POST.get('comments')


        tickets = Ticket(
            ticket_name = ticketName  ,
            ticket_type= ticketType,
            short_desc= shortDesc,
            open_date= dateOpened,
            affected_user= employee.objects.get(id=affUser),
            priority= priority,
            state= state,
            assigned_grp= assGroup,
            assigned_to= User.objects.get(id=assTo),
            email= email,
            comments=comments
        )
        tickets.save()
        return redirect('index')
    return render(request, 'allIssues.html')


def EDIT(request):
    ticket = Ticket.objects.all()
    context  = {
        'ticket':ticket,
    }
    return redirect(request, 'allIssues.html',context)


def Update(request,id):
    if request.method == "POST":
        ticketName = request.POST.get('ticketName')
        ticketType = request.POST.get('ticketType')
        shortDesc = request.POST.get('shortDesc')
        dateOpened = request.POST.get('dateOpened')
        affUser = request.POST.get('affUser')
        priority = request.POST.get('priority')
        state = request.POST.get('state')
        assGroup = request.POST.get('assGroup')
        assTo = request.POST.get('assTo')
        email = request.POST.get('email')
        comments = request.POST.get('comments')

    tickets = Ticket(
            id = id,
            ticket_name = ticketName  ,
            ticket_type= ticketType,
            short_desc= shortDesc,
            open_date= dateOpened,
            affected_user= employee.objects.get(id=affUser),
            priority= priority,
            state= state,
            assigned_grp= assGroup,
            assigned_to= User.objects.get(id=assTo),
            email= email,
            comments=comments
    )
    tickets.save()
    return redirect('index')
    return redirect(request,'allIssues.html')


def Done(request):
    if request.method == "POST":
        return redirect(request, 'allIssues.html')


def DELETE(request,id):
    ticket=Ticket.objects.filter(id = id).delete()
    context ={
         'ticket':ticket,
    }
    return redirect('index')
    return redirect(request,'allIssues.html', context)


def done(request):
    return redirect(request, 'allIssues.html' )


