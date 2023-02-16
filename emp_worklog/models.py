from django.db import models
from django.utils import timezone
from Project.models import Project,SubProject
from django.contrib.auth.models import User

# Create your models here. 

class tasktype(models.Model):
  TaskType=models.CharField(max_length=100, null=False)

  def __str__(self):
      return self.TaskType
  
class worklog(models.Model):
  User = models.ForeignKey(User,on_delete=models.CASCADE)
  Date = models.DateField(default=timezone.now)
  TaskType = models.ForeignKey(tasktype, on_delete=models.CASCADE,default=1)
  project_id = models.ForeignKey(SubProject,on_delete=models.CASCADE,default=1)
  Workdone = models.CharField(max_length=255)
  Hours = models.PositiveIntegerField(default=0)
  Billable = models.BooleanField("Billable", default=False, null=True)



def __str__(self):
      return self.User
  