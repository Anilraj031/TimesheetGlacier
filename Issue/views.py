from django.shortcuts import render
from django.shortcuts import redirect
<<<<<<< HEAD
from . models import Ticket,ticketDetails
=======
from . models import Ticket
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
from Attendance.models import User
from Customer.models import employee
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
# function based views
def index(request):
    allusers =User.objects.all().values('id','username')
    ticket = Ticket.objects.all()
<<<<<<< HEAD
    mytickets = Ticket.objects.filter(assigned_to= request.user)
=======
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
    customer = employee.objects.all().values()
    #print(customer)
    dic = {
        'ticket':ticket,
        'users':list(allusers),
<<<<<<< HEAD
        'customer':list(customer),
        'mytickets':mytickets
=======
        'customer':list(customer)
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
        }
    return render(request, 'Issues/allIssues.html', dic)

def getIssue(request,issueid):
    issue = Ticket.objects.get(id=issueid)
<<<<<<< HEAD
    issueComments = ticketDetails.objects.filter(ticket_id = issueid)
    allusers =User.objects.all().values('id','username')
    customer = employee.objects.all().values()

    #print(issueComments)
    return render(request, 'Issues/details.html',{'issue':issue,'users':allusers,'customer':customer,'comments':issueComments})
=======
    allusers =User.objects.all().values('id','username')
    customer = employee.objects.all().values()
    #print(allusers)
    return render(request, 'Issues/details.html',{'issue':issue,'users':allusers,'customer':customer})
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06

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
<<<<<<< HEAD
        
=======
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06

    tickets = Ticket(
            id = id,
            ticket_name = ticketName  ,
            ticket_type= ticketType,
            short_desc= shortDesc,
            open_date= dateOpened,
            affected_user= employee.objects.get(id=affUser),
            priority= priority,
<<<<<<< HEAD
            state = state,
=======
            state= state,
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
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

@csrf_exempt
def updateStatus(request):
    status=request.POST['status']
    id=request.POST['id']
    print(status)
    if status == 'new':
        Ticket.objects.filter(id=id).update(state='New')
    elif status == 'inprogress':
        Ticket.objects.filter(id=id).update(state='InProgress')
    elif status == 'hold':
        Ticket.objects.filter(id=id).update(state='Hold')
    elif status == 'complete':
        Ticket.objects.filter(id=id).update(state='Completed')
    else:
        Ticket.objects.filter(id=id).update(state='Canceled')
<<<<<<< HEAD
    return JsonResponse({'result':"success"})

@csrf_exempt
def addComments(request):
    if request.method == "POST":
        id = request.POST.get('id')
        #print(id)
        ticket = Ticket.objects.get(id=id)
        comments = request.POST.get('newcomment')

        details = ticketDetails(ticket = ticket, comments = comments,user=request.user)
        details.save()
        
        getComment = ticketDetails.objects.last()
        return JsonResponse({'date':getComment.date.strftime("%B %d, %Y %I:%M %p"),'comment':getComment.comments,'user':getComment.user.username})
=======
    return JsonResponse({'result':"success"})
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
