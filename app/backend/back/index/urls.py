from django.urls import path
from .views import CustomTokenObtainPairView 
from .views import UserRegistration, UserLogin
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('SignUp/', UserRegistration.as_view({'post':'register'})),
    path('SignIn/', UserLogin.as_view({'post':'login'})),
]