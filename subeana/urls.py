from django.contrib import admin
from django.urls import path
from . import views

app_name = 'subeana'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.top, name = 'top'),
    path('new', views.new, name = 'new'),
]