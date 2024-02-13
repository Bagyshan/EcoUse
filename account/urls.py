from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomPasswordConfirmView, RegistrationView, LogoutView, ActivationView, CustomResetPasswordView
from django.urls import path

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uuid:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', CustomResetPasswordView.as_view()),
    path('password_confirm/', CustomPasswordConfirmView.as_view())
]
