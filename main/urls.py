from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('adds/', views.adds),
    path('adds/<int:add_id>', views.add),
    path('users/<int:user_id>', views.user)
]
