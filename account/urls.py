from django.urls import path
from .views import RegistrationView, LogoutView, ActivationView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
