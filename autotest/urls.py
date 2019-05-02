from django.urls import path
from . import views

urlpatterns = [
    path('', views.ResponseListView.as_view(), name='response-list'),
]
