from django.contrib import admin
from django.urls import path
from .views import home, health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health),
]