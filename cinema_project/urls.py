from django.contrib import admin
from django.urls import path
from cinema_project.views import HealthCheckView, SessionListCreateView, SessionDetailView

urlpatterns = [
    path('health', HealthCheckView.as_view()),
    path('api/sessions', SessionListCreateView.as_view()),
    path('api/sessions/<int:pk>', SessionDetailView.as_view()),
]
