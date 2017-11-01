from __future__ import unicode_literals
 
from django.db import models


from ..music_app.models import Song
from ..user_app.models import User

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='playlists')

class Review(models.Model):
    review = models.TextField(max_length=1000)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    song = models.ForeignKey(Song, related_name='reviews')
    user = models.ForeignKey(User, related_name='reviews')

class Addition(models.Model):
    song = models.ForeignKey(Song, related_name='additions')
    playlist = models.ForeignKey(Playlist, related_name='additions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)