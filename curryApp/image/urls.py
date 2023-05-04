from django.urls import path
from . import views

app_name = 'image'

urlpatterns = [
    path('', views.CreateImageView.as_view(), name='home'),
]