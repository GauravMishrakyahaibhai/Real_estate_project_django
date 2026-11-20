from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import SignInForm

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path(
        "signin/",
        auth_views.LoginView.as_view(
            template_name="accounts/signin.html",
            authentication_form=SignInForm,
        ),
        name="signin",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

