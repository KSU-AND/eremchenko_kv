from django.urls import path, include

from .views.login import LoginView
from .views.logout import LogoutView
from .views.profile import ProfileView
from .views.registration import RegistrationView


accounts_url_patterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('registration/', RegistrationView.as_view(), name="registration"),
]
