from django.contrib import admin
from django.urls import path
from tugas3.bodyweight import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', views.DataAPI.as_view(), name='data')
]
