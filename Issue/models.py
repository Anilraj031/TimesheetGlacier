from django.db import models
from django.contrib.auth.models import User
from Customer.models import employee

# Create your models here.
class Ticket(models.Model):
    # ticket_id = models.AutoField(primary_key=True )
    ticket_name= models.CharField(max_length=30)
    ticket_type= models.CharField(max_length=30)
    short_desc= models.CharField(max_length=130,null=True)
    open_date= models.DateField(auto_now=True)
    affected_user= models.ForeignKey(employee,null=True,on_delete=models.SET_NULL)
    #affected_user=models.CharField(max_length=30)
    priority= models.CharField(max_length=30)
<<<<<<< HEAD
    state= models.CharField(max_length=30,default="New",null=True)
=======
    state= models.CharField(max_length=30)
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
    last_updated= models.DateTimeField(auto_now=True)
    assigned_grp= models.CharField(max_length=30,null=True)
    #assigned_to= models.CharField(max_length=30,null=True)
    assigned_to= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    email= models.EmailField(max_length=100,null=True)
    comments= models.CharField(max_length=120,null=True)


    def __str__(self):
<<<<<<< HEAD
        return self.ticket_name


class ticketDetails(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.SET_NULL,null=True)
    comments = models.CharField(max_length=500,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date = models.DateTimeField(auto_now=True)
=======
        return self.ticket_name
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
