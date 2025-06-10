from django.urls import path
from .views import UserRegistration, UserLogin
urlpatterns = [
    path('SignUp/', UserRegistration.as_view({'post':'register'})),
    path('SignIn/', UserLogin.as_view({'post':'login'})),
]