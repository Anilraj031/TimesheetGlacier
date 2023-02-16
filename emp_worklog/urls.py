from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('dailylog1/', views.dailylog1),
    path('billable/', views.billable),
    path('nonbillable/', views.nonbillable),
    path('loginpage/', views.loginpage),
    path('test/', views.test),
    path('enterrecord/', views.enterrecord),
    path('addrecord/', views.addrecord),
    path('dailylog/', views.dailylog, name='dailylog'),
    path('add', views.ADD, name='add'),
    path('edit', views.Edit, name='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path('delete/<str:id>', views.Delete, name='delete'),

    # path('filter/', views.filter)
]
 