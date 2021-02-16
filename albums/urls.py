from django.urls import path
from .views import AlbumListView,AlbumDetailView,PhotoCreateView,AlbumCreateView,AlbumUpdateView,PhotoUpdateView,AlbumDeleteView
urlpatterns = [
    path('albums/<int:pk>/delete/',AlbumDeleteView.as_view(), name='album_delete'),
    path('albums/<int:pk>/editPhoto/',PhotoUpdateView.as_view(),name='photo-edit'),
    path('albums/<int:pk>/edit/',AlbumUpdateView.as_view(),name='album-edit'),
    path('albums/new/',AlbumCreateView.as_view(), name='album_new'),
    path('albums/newphoto/',PhotoCreateView.as_view(), name='photo_new'),
    path('albums/<int:pk>/',AlbumDetailView.as_view(), name='album-detail'),
    path('', AlbumListView.as_view(), name='album-list'),
]