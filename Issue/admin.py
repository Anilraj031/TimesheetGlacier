from django.contrib import admin
<<<<<<< HEAD
from .models import Ticket,ticketDetails
# Register your models here.
class display(admin.ModelAdmin):
    list_display = ('id','ticket_name','ticket_type')
admin.site.register(Ticket,display)

class displayDetails(admin.ModelAdmin):
    list_display = ('ticket','comments','date','user')

admin.site.register(ticketDetails,displayDetails)
=======
from .models import Ticket
# Register your models here.
class display(admin.ModelAdmin):
    list_display = ('id','ticket_name','ticket_type')
admin.site.register(Ticket,display)
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
