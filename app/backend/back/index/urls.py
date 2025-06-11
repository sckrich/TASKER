from django.urls import path
from .views import CustomTokenObtainPairView 
from .views import UserRegistration, UserLogin, UserGroups
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('SignUp/', UserRegistration.as_view({'post':'register'})),
    path('SignIn/', UserLogin.as_view({'post':'login'})),
    path('groups/', UserGroups.as_view({'post':'getGroups'}))
]