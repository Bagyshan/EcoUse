from django.urls import path
from .views import CustomPasswordConfirmView, RegistrationView, LogoutView, ActivationView, CustomResetPasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    # path('password_reset/', CustomResetPasswordView.as_view(), name='password_reset'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reset_password/', CustomResetPasswordView.as_view()),
    path('password_confirm/<uidb64>/', CustomPasswordConfirmView.as_view())
]
