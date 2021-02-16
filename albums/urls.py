from django.urls import path
from .views import AlbumListView,AlbumDetailView,PhotoCreateView
urlpatterns = [
    path('albums/new/',PhotoCreateView.as_view(), name='album_new'),
    path('albums/<int:pk>/',AlbumDetailView.as_view(), name='album-detail'),
    path('', AlbumListView.as_view(), name='album-list'),
]