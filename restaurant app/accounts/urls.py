from django.urls import path
from . import views
urlpatterns = [
    path('register-user', view=views.register_user, name='register-user'),
    path('register-restaurant', view=views.register_restaurant, name='register-restaurant'),
    path('login/', view=views.login, name='login'),
    path('logout/', view=views.logout, name='logout'),
    path('dashboard/', view=views.dashboard, name='dashboard'),
]
