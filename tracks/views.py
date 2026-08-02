
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Music

# READ: Displays all the songs in the database
class MusicListView(ListView):
    model = Music
    template_name = 'tracks/music_list.html'
    context_object_name = 'tracks'  # This is the variable name we will use in the HTML file
    ordering = ['-add_date']        # The minus sign means "Newest first"

# CREATE: Displays the upload form and saves new songs
class MusicCreateView(CreateView):
    model = Music
    # Notice we do NOT include 'add_date' because auto_now_add handles it automatically!
    fields = ['title', 'artist', 'genre', 'audio_file']
    template_name = 'tracks/music_form.html'
    success_url = reverse_lazy('music_list')  # Where to go after successfully uploading

# UPDATE: Displays the form with existing data to edit a song
class MusicUpdateView(UpdateView):
    model = Music
    fields = ['title', 'artist', 'genre', 'audio_file']
    template_name = 'tracks/music_form.html'
    success_url = reverse_lazy('music_list')

# DELETE: Asks for confirmation and deletes the song
class MusicDeleteView(DeleteView):
    model = Music
    template_name = 'tracks/music_confirm_delete.html'
    success_url = reverse_lazy('music_list')