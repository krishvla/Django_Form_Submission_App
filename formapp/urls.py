from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('incidents/', views.Incidents.as_view(), name='incidents'),
]