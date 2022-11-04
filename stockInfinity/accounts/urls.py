from django.urls import path
from . import views

urlpatterns = [
        path('signup/', views.signup.as_view(), name="signup"),
        ]

