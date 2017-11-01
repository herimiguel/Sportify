from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [

    url(r'^', include('apps.user_app.urls', namespace='user_app')),
    url(r'^music/', include('apps.music_app.urls', namespace='music_app')),
    url(r'^playlist/', include('apps.playlist_app.urls', namespace='playlist_app')),

]

