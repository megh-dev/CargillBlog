from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Cargill_blog, name='Cargill-blog'),
    path('about/', views.Cargill_about, name='Cargill-about'),
]