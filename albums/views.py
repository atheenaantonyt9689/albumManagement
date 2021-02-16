from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView

# Create your views here.
from .models import Album,Photo

class AlbumListView(ListView):

    model =Album
    template_name = "albums/album-list.html"

class AlbumDetailView(DetailView):
    model = Album
    template_name='albums/album-detail.html'

class PhotoCreateView(CreateView):
    model = Photo
    template_name='albums/album_new.html'
    fields='__all__'


