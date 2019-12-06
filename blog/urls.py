from django.urls import include, path
from . import views

app_name='blog'
urlpatterns = [
    path('', views.greeting),
    path('morning/', views.morning_greeting),
    path('evening/', views.evening_greeting),
    path('<int:pk>/edit/', views.post_edit),
    path('posts/', views.index),


]