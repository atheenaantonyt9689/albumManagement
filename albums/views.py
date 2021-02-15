from django.views.generic import ListView,DetailView

# Create your views here.
from .models import Album,Photo

class AlbumListView(ListView):

    model =Album
    template_name = "albums/album-list.html"

class AlbumDetailView(DetailView):
    model = Album
    template_name='albums/album-detail.html'

#class PhotoDetailView(DetailView):
    #model = Photo
    #template_name='albums/album-detail.html'


