"""av URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core.dashboard.views import DashboardView
from core.homepage.views import IndexView
from core.login.views import *
# from views.dd.views import DdView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('login/', include('core.login.urls'), name='login'),
    path('encuesta/', include('core.encuesta.urls'), name='encuesta'),
    # path('user/', include('user.urls')),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path("select2/", include("django_select2.urls")),
    # path('dd/', DdView.as_view(), name='dd')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
