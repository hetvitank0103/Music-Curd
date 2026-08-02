
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Music

# READ: Displays all the songs in the database
class MusicListView(ListView):
    model = Music
    template_name = 'tracks/music_list.html'
    context_object_name = 'tracks'

    def get_queryset(self):
        # 1. Start by ordering everything alphabetically by the 'title' field
        queryset = Music.objects.all().order_by('title')
        
        # 2. Check if the user typed anything into our search box
        search_keyword = self.request.GET.get('search')
        if search_keyword:
            # 3. Filter the results (icontains means "case-insensitive match")
            queryset = queryset.filter(title__icontains=search_keyword)
            
        return queryset
    
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