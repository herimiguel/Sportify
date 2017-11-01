from __future__ import unicode_literals
 
from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    artist_bio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Album(models.Model):
    album_name = models.CharField(max_length=255)
    album_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    artist = models.ForeignKey(Artist, related_name="albums")

class Song(models.Model):
    song_name = models.CharField(max_length=(255))
    song_year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    album = models.ForeignKey(Album, related_name="songs")


    