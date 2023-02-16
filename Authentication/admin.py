from django.contrib import admin
from Authentication.models import LoggedUser,Company,Employees

# Register your models here.
#@admin.site.register(LoggedUser)
class LoggedAdmin(admin.ModelAdmin):
    list_display=('id','user')

class compAdmin(admin.ModelAdmin):
    list_display=('user','name','address','phone1','phone2','email','contact_email')

class userCompAdmin(admin.ModelAdmin):
    list_display = ('company','user')

admin.site.register(Employees,userCompAdmin)
admin.site.register(LoggedUser,LoggedAdmin)
admin.site.register(Company,compAdmin)