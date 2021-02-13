from django.urls import path
from .views import AlbumListView,AlbumDetailView
urlpatterns = [
    path('albums/<int:pk>/',AlbumDetailView.as_view(), name='album-detail'),
    path('', AlbumListView.as_view(), name='album-list'),
]