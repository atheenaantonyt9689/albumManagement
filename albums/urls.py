from django.urls import path
from .views import AlbumListView
urlpatterns = [
path('', AlbumListView.as_view(), name='album-list'),
]