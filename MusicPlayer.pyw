# import libs
import os
import pygame
from mutagen.mp3 import MP3
import time
import random
import asyncio

# init program
os.chdir('/Users/snowman/Desktop/Code/Music/All Songs/')
usedAlbums = []
usedSongs = []
vol = float(input("Enter the volume (Between 0 and 1): "))
albums = os.listdir()
albums.remove('.DS_Store')
random.shuffle(albums)
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)

# define funcs
def addAlbum():

    currentAlbum = albums[album]

    if currentAlbum in usedAlbums:
        addAlbum()
    else:
        usedAlbums.append(currentAlbum)

    return currentAlbum

def addSong():

    currentSong = songs[song]

    if currentSong in usedSongs:
        addSong()
    else:
        usedSongs.append(currentSong)
    
    return currentSong

async def wait(songlen):
    await asyncio.sleep(songlen.info.length)

# begin main code
for album in range(len(albums)):
    # get new or starter album(s)
    currentAlbum = addAlbum()
    os.chdir(currentAlbum)
    songs = os.listdir()
    random.shuffle(songs)
    song = 0
    for song in range(len(songs)):
        # get new or starter song(s)
        currentSong = addSong()
        songinfo = MP3(currentSong)
        pygame.mixer.init(frequency=songinfo.info.sample_rate, size=-16, channels=2, buffer=4096)
        pygame.mixer.music.set_volume(vol)
        pygame.mixer.music.load(currentSong)
        pygame.mixer.music.play()
        # print info
        print("~" * 80)
        print("Total Songs Played:", song + 1)
        print("Album:             ", currentAlbum)
        print("Album Songs:       ", len(songs))
        print("Song number:       ", len(usedSongs))
        print("Songs left:        ", len(songs) - (song + 1))
        print("Song:              ", currentSong[:-4])
        print("Duration:          ", str(int(songinfo.info.length // 60)) + ":%02d" % int(songinfo.info.length % 60))
        print("~" * 80)
        asyncio.run(wait(songinfo))
    os.chdir('/Users/snowman/Desktop/Code/Music/All Songs/')