"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, URLPattern
from typing import List

from .views import HomePageView, UserLoginView, UserLogoutView
from .constants import HOME, LOGIN, LOGOUT


urlpatterns: List[URLPattern] = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Home page:
    path('', HomePageView.as_view(), name=HOME),

    # Authentication:
    path('login/', UserLoginView.as_view(), name=LOGIN),
    path('logout/', UserLogoutView.as_view(), name=LOGOUT),

    # Apps:
    path('users/', include('task_manager.users.urls'))
]
