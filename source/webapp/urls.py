from django.urls import path
from webapp.views import IndexView,  PictureView, PictureCreateView, PictureUpdateView, PictureDeleteView
app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('picture/<int:pk>/', PictureView.as_view(), name='picture_view'),
    path('picture/add/', PictureCreateView.as_view(), name='picture_create'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture_update'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete'),
]
