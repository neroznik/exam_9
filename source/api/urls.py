from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import RegisterView, RegisterActivateView, UserDetailView, \
    UserChangeView, UserPasswordChangeView, UserPasswordResetEmailView, UserPasswordResetView
from api.views import AddFavSet, RemoveFavSet, get_token_view

app_name = 'api'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('favorite/', AddFavSet.as_view(), name='picture_favorite'),
    path('unfavorite/', RemoveFavSet.as_view(), name='picture_unfavorite'),
]
