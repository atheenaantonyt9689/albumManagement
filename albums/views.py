from django.views.generic import ListView

# Create your views here.
from .models import Album

class AlbumListView(ListView):

    model =Album
    template_name = "albums/album-list.html"