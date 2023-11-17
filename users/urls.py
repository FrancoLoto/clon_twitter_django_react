from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('u/search/', views.search),
    path('reco/', views.reco),
    path('follow/<str:username>/', views.follow),
    path('register/', views.register),
    path('login/', views.MyTokenObtainPairSerializer.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('<str:username>/', views.UserDetailView.as_view()),
]
