from django.urls import path
from . import views
urlpatterns = [
    path('register-user', view=views.register_user, name='register-user'),
    path('register-restaurant', view=views.register_restaurant, name='register-restaurant'),
    path('login/', view=views.login, name='login'),
    path('logout/', view=views.logout, name='logout'),
    path('user-dashboard/', view=views.customer_dashboard, name='customer-dashboard'),
    path('vendor-dashboard/', view=views.vendor_dashboard, name='vendor-dashboard'),
    path('my-account/', view=views.my_account, name='my-account'),
    path('activate/<uidb64>/<token>/', view=views.activate, name='activate'),
]
