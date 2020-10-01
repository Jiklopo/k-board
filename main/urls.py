from django.urls import path
from main import views_adds, views_users, views

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('message', views.MessageView.as_view(), name='message'),

    path('adds/', views_adds.AddsListView.as_view(), name='adds'),
    path('adds/top', views_adds.TopAddsListView.as_view(), name='top_adds'),
    path('adds/<int:pk>/', views_adds.AddDetailView.as_view(), name='add_detail'),
    path('adds/<int:pk>/edit', views_adds.AddUpdateView.as_view(), name='add_update'),
    path('adds/<int:pk>/delete', views_adds.AddDeleteView.as_view(), name='add_delete'),
    path('adds/new/', views_adds.AddFormView.as_view(), name='new_add'),

    path('login/', views_users.LoginView.as_view(), name='login'),
    path('logout/', views_users.LogoutView.as_view(), name='logout'),
    path('register/', views_users.RegistrationView.as_view(), name='register'),
    path('password_change', views_users.ChangePasswordView.as_view(), name='change_password'),
    path('profile/', views_users.ProfileView.as_view(), name='profile'),
    path('profile/edit', views_users.ProfileEditView.as_view(), name='profile_edit'),

]
