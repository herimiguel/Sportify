# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from models import *
from ..playlist_app.models import Playlist

def index(request):
    context={
        'artists': Artist.objects.all(),
        'playlists': Playlist.objects.all()
    }
    return render(request, 'music_app/index.html', context)

def createArtist(request):
    if request.method == 'POST':
        artist_name= request.POST['artist_name']
        artist_bio= request.POST['artist_bio']
        isValid = True
        minVal = 2
    if len(request.POST['artist_name']) < minVal:
        messages.error(request, "Artist Name must be at least two Characters!")
        isValid = False
    if len(request.POST['artist_bio']) < minVal:
        messages.error(request, "Artist Bio must be at least two Characters!")
        isValid = False
    if not isValid:
        return redirect('music_app:addArtist')
    else:
        Artist.objects.create(artist_name=artist_name, artist_bio=artist_bio)        
        return redirect('music_app:index')

def addArtist(request):
    return render(request, 'music_app/addArtist.html')

def viewArtist(request, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id),
        'albums': Album.objects.filter(artist_id=artist_id),
    }
    return render(request, 'music_app/displayArtist.html', context)

def editArtist(request, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id)
    }
    return render(request, 'music_app/editArtist.html', context)

def updateArtist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.artist_name= request.POST['artist_name']
    artist.artist_bio= request.POST['artist_bio']
    artist.save()
    return redirect('music_app:index')

def deleteArtist(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.delete()
    return redirect('music_app:index')

# ************************
# ************************

def addAlbum(request, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id),
        'albums': Album.objects.filter(artist_id=artist_id)
    }
    return render(request, 'music_app/albumCreate.html', context)
    
def createAlbum(request, artist_id):
    if request.method == 'POST':
        artist= Artist.objects.filter(id=artist_id).order_by('artist_name')
        album_name= request.POST['album_name']
        album_year= request.POST['album_year']
        isValid = True
        minVal = 2
    if len(request.POST['album_name']) < minVal:
        messages.error(request, "Album Name must be at least two Characters!")
        isValid = False

    if len(request.POST['album_year']) < minVal:
        messages.error(request, "album Year must be at least 2 Characters!")
        isValid = False
    if not isValid:
        return redirect(reverse('music_app:addAlbum', kwargs={'artist_id': artist_id}))
    else:
        Album.objects.create(album_name= album_name, album_year= album_year, artist_id=artist_id)
        return redirect(reverse('music_app:viewArtist', kwargs={'artist_id': artist_id}))

def viewAlbum(request):
    return render(request, 'playlist_app/index.html')

def updateAlbum(request):
    return render(request, 'playlist_app/index.html')

def deleteAlbum(request, album_id, artist_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect(reverse('music_app:viewArtist', kwargs={'artist_id': artist_id}))

def addSong(request, album_id, artist_id):
    context={
        'artist': Artist.objects.get(id=artist_id),
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album_id=album_id)        
    }
    return render(request, 'music_app/songs.html', context)

def createSong(request, album_id, artist_id):    
    if request.method == 'POST':
        album= Album.objects.get(id=album_id)
        artist= Artist.objects.get(id=artist_id)
        song_name= request.POST['song_name']
        song_year= request.POST['song_year']
        isValid = True
        minVal = 2
    if len(request.POST['song_name']) < minVal:
        messages.error(request, "Song Name must be at least two Charactoers!")
        isValid= False
    if len(request.POST['song_year']) < minVal:
        messages.error(request, "Song Year must be at least two characters")
        isValid = False
    if not isValid:
        return redirect(reverse('music_app:addSong', kwargs={ 'artist_id': artist_id, 'album_id': album_id }))
    else:
        Song.objects.create(song_name= song_name, song_year= song_year, album_id=album_id)
        return redirect(reverse('music_app:addSong', kwargs={'artist_id': artist_id, 'album_id':album_id}))


def viewSong(request, song_id):
    context={
        'song': Song.objects.get(id=song_id),
        # 'album': Album.objects.get(id=album_id),
        'album': Album.objects.filter(id=song_id)
    }
    return render(request, 'music_app/displaySong.html', context)

def deleteSong(request, album_id, song_id):
    song = Song.objects.get(id=song_id)
    song.delete()
    return redirect(reverse('music_app:index'))

def updateSong(request):
    return render(request, 'playlist_app/index.html')

def allSongs(request, playlist_id):
    song= Song.objects.all()
    context={
        'songs': song,
        'playlist_id': playlist_id
    }
    return render(request, 'music_app/allSongs.html', context)

# ************************

def search(request):
    return render(request, 'playlist_app/index.html')

def newRelease(request):
    return render(request, 'playlist_app/index.html')