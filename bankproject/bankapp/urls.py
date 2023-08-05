from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('branches/', views.branches, name="branches"),
    path('booking/', views.booking, name="booking"),
    path('department/', views.department, name="departments"),
]