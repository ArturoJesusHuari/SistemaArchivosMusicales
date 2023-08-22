import pytube
import config as cfg
import os
from os import system
import pathlib
from colorama import Fore
import pytube as pt
def Direction(autor):
    return str(pathlib.Path(__file__).parent.absolute()).replace('funciones','songs')+'/'+autor+'/'
def Download(link):
    try:
        yt = pt.YouTube(link)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(Direction(yt.author))
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except pytube.exceptions.VideoUnavailable:
        pass
def formatAudioClip(string):
    years = [str(num) for num in range(1950,2100)]
    listWords = years + ['(',')'
                ,'Official','Video','Español','//'
                ,'Letra','Music','4K','Sub.','Sub'
                ,'Remaster','[',']','HD','Visualizer',
                'Lyric','Remix','Version','Audio',
                'On','MTV','Unplugged','Unedited',
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