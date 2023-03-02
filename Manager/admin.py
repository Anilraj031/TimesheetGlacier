from django.contrib import admin
from Manager.models import InitialPassword

# Register your models here.
class InitialPasswordAdmin(admin.ModelAdmin):
    list_display=('id','user','first_password','first_changed')


admin.site.register(InitialPassword,InitialPasswordAdmin)