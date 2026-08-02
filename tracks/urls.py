# tracks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/ -> Shows the list of all songs
    path('', views.MusicListView.as_view(), name='music_list'),
    
    # http://127.0.0.1:8000/add/ -> Shows the upload form
    path('add/', views.MusicCreateView.as_view(), name='music_create'),
    
    # http://127.0.0.1:8000/1/edit/ -> Shows the form to edit song #1
    path('<int:pk>/edit/', views.MusicUpdateView.as_view(), name='music_update'),
    
    # http://127.0.0.1:8000/1/delete/ -> Asks to confirm deleting song #1
    path('<int:pk>/delete/', views.MusicDeleteView.as_view(), name='music_delete'),
]