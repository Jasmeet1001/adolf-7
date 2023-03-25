from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login_check, name='login-view'),  # type: ignore
    path('', views.loginTry, name='login-view'),  # type: ignore
]