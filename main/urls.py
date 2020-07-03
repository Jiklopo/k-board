from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('adds/', views.adds, name='adds'),
    path('adds/<int:add_id>', views.add, name='add_detail'),
    path('adds/new/', views.add_form, name='new_add'),

    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/<int:user_id>', views.user, name='user_detail')
]
