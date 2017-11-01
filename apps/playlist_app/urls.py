from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^addPlaylist$', views.addPlaylist, name='addPlaylist'),
    url(r'^createPlaylist$', views.createPlaylist, name='createPlaylist'),
    url(r'^(?P<playlist_id>\d+)/viewPlaylist$', views.viewPlaylist, name='viewPlaylist'),
    url(r'^(?P<song_id>\d+)/addToPlaylist/(?P<playlist_id>\d+)$', views.addToPlaylist, name='addToPlaylist'),
    url(r'^(?P<playlist_id>\d+)/deletePlaylist$', views.deletePlaylist, name="deletePlaylist"),
]       





# url(r'^$', views.index, name='index'),
#     url(r'^createArtist$', views.createArtist, name='createArtist'),
#     url(r'^addArtist$', views.addArtist, name='addArtist'),
#     url(r'^(?P<artist_id>\d+)/viewArtist$', views.viewArtist, name='viewArtist'),
#     url(r'^(?P<artist_id>\d+)/updateArtist$', views.updateArtist, name='updateArtist'),
#     url(r'^(?P<artist_id>\d+)/editArtist$', views.editArtist, name='editArtist'),
#     url(r'^(?P<artist_id>\d+)/deleteArtist$', views.deleteArtist, name='deleteArtist'),
#     url(r'^(?P<artist_id>\d+)/addAlbum$', views.addAlbum, name='addAlbum'),
#     url(r'^(?P<artist_id>\d+)/createAlbum$', views.createAlbum, name='createAlbum'),
#     url(r'^(?P<album_id>\d+)/viewAlbum$', views.viewAlbum, name='viewAlbum'),
#     url(r'^(?P<album_id>\d+)/updateAlbum$', views.updateAlbum, name='updateAlbum'),
#     url(r'^(?P<album_id>\d+)/(?P<artist_id>\d+)/deleteAlbum$', views.deleteAlbum, name='deleteAlbum'),
#     url(r'^(?P<album_id>\d+)/(?P<artist_id>\d+)/addSong$', views.addSong, name='addSong'),    
#     url(r'^(?P<album_id>\d+)/(?P<artist_id>\d+)/createSong$', views.createSong, name='createSong'),