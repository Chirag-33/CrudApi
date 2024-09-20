from django.urls import path
from django.http import HttpResponse
from . import views
urlpatterns = [
    path('',views.home,name=''),
    path('register',views.register,name='register'),
    path('my-login',views.mylogin,name='my-login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user-logout',views.my_logout, name='user-logout'),
    path('create-record', views.create_record,name='create-record'),
    path('update-record<int:pk>',views.Update_Record,name='update-record'),
    path('view-record/<int:pk>', views.view_record,name='view-record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record')
]