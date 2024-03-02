from django.urls import path
from . import views

app_name = 'account-register'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('sign-in/', views.sign_in, name='signin'),
    path('log-out/', views.log_out, name='logout')
]
