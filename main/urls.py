from django.urls import path
from main import views_adds, views_users, views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(template_name='index.html'), name='index'),
    path('adds/', views_adds.AddsListView.as_view(template_name='adds/adds.html'), name='adds'),
    path('adds/<int:pk>/', views_adds.AddDetailView.as_view(template_name='adds/add.html'), name='add_detail'),
    path('adds/<int:pk>/edit', views_adds.AddUpdateView.as_view(template_name='adds/form.html'), name='add_update'),
    path('adds/new/', views_adds.AddFormView.as_view(template_name='adds/form.html'), name='new_add'),

    path('login/', views_users.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views_users.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', views_users.RegistrationView.as_view(template_name='users/register.html'), name='register')
]
