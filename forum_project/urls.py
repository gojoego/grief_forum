from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('forum.urls')),
    path('guidelines/', TemplateView.as_view(template_name="forum/guidelines.html"), name="guidelines")
]
