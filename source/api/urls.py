from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, RegisterActivateView, UserDetailView, \
    UserChangeView, UserPasswordChangeView, UserPasswordResetEmailView, UserPasswordResetView
from api.views import AddFavSet, RemoveFavSet, get_token_view

app_name = 'api'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('like/', AddFavSet.as_view(), name='picture_like'),
    path('unlike/', RemoveFavSet.as_view(), name='picture_unlike'),
]
