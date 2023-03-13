from django.urls import path
from task_app import views

app_name = 'task_app'

urlpatterns= [

    path('lista/', views.task_list, name= 'task_list'),
    path('create/', views.task_create, name= 'task_create'),
    path('detail/', views.task_detail, name= 'task_detail'),
    path('delete/', views.task_delete, name= 'task_delete'),
    path('<int:id>/', views.task_read, name= 'task_read'),

]