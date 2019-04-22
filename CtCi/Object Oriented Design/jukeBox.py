# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

#  Juke Box

class Song:
    def __init__(self, title, length, artist):
        self.title = title
        self.length = length
        self.artist = artist

class Artist:
    def __init__(self, name):
        self.name = name

class CD:
    def __init__(self, title, artist, songList):
        self.title = title
        self.artist = artist
        self.songList = songList

class Jukebox:
    def __init__(self, cd):
        self.cd = cd
        
