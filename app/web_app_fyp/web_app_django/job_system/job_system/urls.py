"""job_system URL Configuration

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
from django.urls import path, include

from recommendation.views import calculate_top_applied_jobs

urlpatterns = [
	path('', include('main_pages.urls')),
    path('authentication/', include('django.contrib.auth.urls')),
    path('accounts/', include('authentication.urls')),
	path('schools/', include('schools.urls')),
    path('job_system/', include('job_system_module.urls')),
    path('admin/', admin.site.urls),
]

calculate_top_applied_jobs(repeat=3600, repeat_until=None)
