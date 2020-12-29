from django.urls import path
from .views import registrationPage, loginPage, logoutAction

urlpatterns = [
    path('registration/', registrationPage, name='registration'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutAction, name='logout'),
]