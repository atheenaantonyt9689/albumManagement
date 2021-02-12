from django.views.generic import ListView,DetailView

# Create your views here.
from .models import Album

class AlbumListView(ListView):

    model =Album
    template_name = "albums/album-list.html"

class AlbumDetailView(DetailView):
    model=Album
    template_name='albums/album-detail.html'

