from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy 

# Create your views here.
from .models import Album,Photo

class AlbumListView(ListView):

    model =Album
    template_name = "albums/album-list.html"

class AlbumDetailView(DetailView):
    model = Album
    template_name='albums/album-detail.html'

class PhotoDetailView(DetailView):

    model = Photo
    template_name='albums/album-detail.html'
#create functions

class AlbumCreateView(CreateView):
    model = Album
    template_name='albums/album_new.html'
    fields='__all__'

class PhotoCreateView(CreateView):
    model = Photo
    template_name ='albums/photo_new.html'
    fields='__all__'


#update functions
class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'albums/album-edit.html'
    fields = ['title','description']

class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'albums/photo-edit.html'
    fields = ['image_url','description','posted_at']

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'albums/album_delete.html'
    success_url = reverse_lazy('album-list')