from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls), # Default admin path
    path('', RedirectView.as_view(url='analytics/', permanent=False), name='home'),
    path('analytics/', include('dashboard.urls')),
]
