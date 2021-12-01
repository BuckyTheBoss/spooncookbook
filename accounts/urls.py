from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from. import views

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('profile/update/', views.UpdateProfile.as_view(), name='update_profile'),
]