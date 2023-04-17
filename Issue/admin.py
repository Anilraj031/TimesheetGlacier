from django.contrib import admin
from .models import Ticket
# Register your models here.
class display(admin.ModelAdmin):
    list_display = ('id','ticket_name','ticket_type')
admin.site.register(Ticket,display)