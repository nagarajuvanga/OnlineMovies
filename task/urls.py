"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from task import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name="main"),
    path('login/',views.login,name="login"),
    path('save_login/',views.save_login,name='save_login'),
    path('savemovie/',views.savemovie,name="savemovie"),
    path('signuppage/', views.signuppage, name="signuppage"),
    path('savesignup/', views.savesignup, name="savesignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userloginhome/', views.userloginhome, name="userloginhome"),
    path('searchaction/', views.searchaction, name="searchaction"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)