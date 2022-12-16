from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from .views import ProfileView


urlpatterns = [
    path('profile/user/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/change_password.html'),
         name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_changed.html'),
         name='password_change_done'),
]
