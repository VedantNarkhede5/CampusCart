from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('profile-setup/', views.profile_setup, name='profile_setup'),
    path('logout/', views.logout_view, name='logout'),
    path( 'seller-profile/<int:user_id>/', views.seller_profile, name='seller_profile'),
    path( 'edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/', views.my_profile, name='my_profile'
),
]