"""
URL configuration for siren_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import home_views, settings_views

urlpatterns = [
    path('', home_views.home_view, name='home_view'),
    path("", include("powermapui.urls")),
    path("", include("powermatchui.urls")),
    path("", include("powerplotui.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('settings/<str:sw_context>/', settings_views.settings_view, name='settings'),
    path('settings/<str:sw_context>/update/<int:pk>/', settings_views.settings_view, name='settings_update'),
    path('settings/<str:sw_context>/delete/<int:pk>/', settings_views.settings_view, name='settings_delete'),
]
urlpatterns += staticfiles_urlpatterns()