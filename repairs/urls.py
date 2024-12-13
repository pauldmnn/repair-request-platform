from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.post_request, name='post_request'),
    path('recent/', views.recent_requests, name='recent_requests'),
]