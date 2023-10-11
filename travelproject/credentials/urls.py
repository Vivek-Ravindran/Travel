from . import views
from django.urls import path



urlpatterns = [

    path('register',views.register,name='register'),
    #path('add/',views.addition,name='addition')
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]