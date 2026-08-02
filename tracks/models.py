from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    add_date = models.DateField(auto_now_add=True)
    audio_file = models.FileField(upload_to='music_files/')
    
    def __str__(self):
        return self.title