"""personal_portfolio URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import home_view, experience_view, skills_view, education_view, interests_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path("contact/", include("contact.urls")),
    path('', home_view, name = "index"),
    path('experience/', experience_view, name = 'experience'),
    path('skills/', skills_view, name = 'skills'),
    path('education/', education_view, name = 'education'),
    path('interests/', interests_view, name = 'interests'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
