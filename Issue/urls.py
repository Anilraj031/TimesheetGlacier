from django.urls import path
from . import views




urlpatterns= [
 
    path('', views.index, name='index'),
    path('add', views.ADD, name = 'add' ),
    path('details/<issueid>',views.getIssue,name='issueDetails'),
    path('edit', views.EDIT, name ='edit'),
    path('update/<str:id>', views.Update, name= 'Update'),
    path('delete/<id>', views.DELETE, name = 'delete'),
    path('donestatus ', views.Done, name='done'),
    path('updateStatus',views.updateStatus,name='updateTicketStatus'),
<<<<<<< HEAD
    path('addDetails', views.addComments, name= 'addComments'),
=======
>>>>>>> 682bbb611b2775ec604603858dc62bbe1a206d06
   
]

