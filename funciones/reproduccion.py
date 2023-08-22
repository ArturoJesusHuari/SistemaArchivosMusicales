import pygame
import os
import sys
from time import sleep
from os import system, path
from .download import *
class SAM:
    #Sistema de archivos musicales
    def __init__(self):
        pygame.mixer.init()
        self.bands = dict(enumerate(os.listdir(os.getcwd()+'/songs/'),start=1))
    def clear(self):
        if(os.name =='nt'):
            pass
            #system('cls')
        elif(os.name =='posix'):
            system('clear')
    def playSound(self,sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    def pauseSound(self):
        pygame.mixer.music.pause()
    def unpauseSound(self):
        pygame.mixer.music.unpause()
    def stopSound(self):
        pygame.mixer.music.stop()
    def quitPygame(self):
        pygame.mixer.quit()
    def home(self):
        self.viewBands()
        inp = input('>>')
        if(inp == 'exit'):
            self.quitPygame()
        else:
            try:
                self.selectionBand(int(inp))
            except:
                Download(inp)
                self.home()
    def viewBands(self):
        self.clear()
        print('SAM')
        self.__init__()
        for key in self.bands:
            print(key,self.bands[key])
    def selectionBand(self,selection):
        try:
            self.songsFrom(self.bands[selection])
        except:
            self.viewBands()
    def songsFrom(self,band):
        self.clear()
        songs = dict(enumerate(os.listdir(os.getcwd()+'/songs/'+band+'/'),start=1))
        for key in songs:
            name, ext = os.path.splitext(songs[key])
            print(key,songs[key].replace('.mp3',''))
        self.selectionSong(band,songs)
    def selectionSong(self,band,songs):
        selection = input('--')
        if(selection=='back'):
            self.selectionBand()
        print(os.getcwd()+'/songs/'+band+'/'+songs[int(selection)])
        try:
            self.playSound(os.getcwd()+'/songs/'+band+'/'+songs[int(selection)])
            self.control(songs[int(selection)])
        except:
            self.songsFrom(band)
    def control(self,name):
        print(name)
        command = input('>> ')
        if command == "p":
            self.pauseSound()
            self.control(name)
        elif command == "c":
            self.unpauseSound()
            self.control(name)
        elif command == "s":
            self.stopSound()
            self.home()
        elif command == "e":
            self.stopSound()
            self.quitPygame()
            exit()
        else:
            self.control(name)

