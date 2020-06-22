from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<category>", views.project_category, name="project_category"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)