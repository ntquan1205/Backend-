from django.contrib import admin
from django.urls import path
from cinema_app.views import HealthCheckView, SessionListCreateView, SessionDetailView, TicketListCreateView, RegisterView, MeView

urlpatterns = [
    path('health', HealthCheckView.as_view()),
    path('api/sessions', SessionListCreateView.as_view()),
    path('api/sessions/<int:pk>', SessionDetailView.as_view()),
    path('api/sessions/<int:session_id>/tickets', TicketListCreateView.as_view()),
    path('auth/register', RegisterView.as_view()),
    path('auth/me', MeView.as_view()),
]
