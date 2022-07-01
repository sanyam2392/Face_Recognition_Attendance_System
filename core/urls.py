from django.urls import path,include
from .views import *


urlpatterns = [
    path('', index, name= 'index'),
    path('ajax/', ajax, name= 'ajax'),
    path('scan',scan,name='scan'),
    path('profiles/', profiles, name= 'profiles'),
    path('details/', details, name= 'details'),

    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('view_profile/<int:id>/',view_profile,name='view_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),


    path('clear_history/',clear_history,name='clear_history'),
    path('report/',report,name='report'),
    path('reset/',reset,name='reset'),

    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),   
	path('logout/', logoutUser,name="logout"),


]
