import pytube
from pytube import YouTube
import config as cfg
from os import system
import pathlib
from moviepy.editor import *
from colorama import Fore
def Direction(autor):
    return str(pathlib.Path(__file__).parent.absolute()).replace('funciones','songs')+'/'+autor+'/'
def YT(link):
    return YouTube(str(link))
def Download(link):
    yt = YT(link)
    try:
        Descarga = yt.streams.get_audio_only().download(Direction(yt.author))
        audioclip = AudioFileClip(Descarga)
        audioclip.write_audiofile(formatAudioClip(audioclip.filename))
        os.remove(audioclip.filename)
    except pytube.exceptions.VideoUnavailable:
        pass
def formatAudioClip(string):
    years = [str(num) for num in range(1950,2100)]
    listWords = years + ['(',')'
                ,'Official','Video','Español','//'
                ,'Letra','Music','4K','Sub.','Sub'
                ,'Remaster','[',']','HD','Visualizer',
                'Lyric','Remix','Version','Audio',
                'Live','On','MTV','Unplugged','Unedited',
                'Edit','edit','|','Alternate','-']
    for word in listWords:
        string = string.replace(word,'')
    string = string.replace('.mp4', '.mp3')
    while True:
        if(string[-5]==' '):
            string = string[0:-6]+'.mp3'
        else:
            break
    return string