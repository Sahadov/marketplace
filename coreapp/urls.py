"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static 
from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path("", views.main_page, name="mainpage"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='coreapp/login.html', authentication_form = LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page="core:mainpage"), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
