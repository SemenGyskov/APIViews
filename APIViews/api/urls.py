from django.urls import path
from . import  views

urlpatterns = [
    path('', views.MenAPIView.as_view()),
    path('<int:pk>/',views.MenAPIView.as_view()),
]