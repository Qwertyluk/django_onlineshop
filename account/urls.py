from django.urls import path
from .views import registrationPage, loginPage, logoutAction, manage, changePassword

urlpatterns = [
    path('registration/', registrationPage, name='registration'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutAction, name='logout'),
    path('manage/', manage, name='manage'),
    path('change-password/', changePassword, name='changePassword')
]