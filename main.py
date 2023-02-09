from pytube import YouTube
import config as cfg
from os import system
import pathlib
from moviepy.editor import *
from colorama import Fore

def Direccion():
    return str(pathlib.Path(__file__).parent.absolute())

def YT(link):
    return YouTube(str(link))

def Download(link):
    yt = YT(link)
    Descarga = yt.streams.get_audio_only().download(Direccion())
    audioclip = AudioFileClip(Descarga)
    audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))
    os.remove(audioclip.filename)

def main():
    ext=False
    while(not ext):
        system("cls")
        print(Fore.CYAN + """
 ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗     ███╗   ███╗██╗   ██╗███████╗██╗ ██████╗
 ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗    ████╗ ████║██║   ██║██╔════╝██║██╔════╝
 ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║    ██╔████╔██║██║   ██║███████╗██║██║     
 ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║    ██║╚██╔╝██║██║   ██║╚════██║██║██║     
 ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝    ██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗
 ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝
    """+ Fore.YELLOW)
        system("dir /B *.mp3")
        intp = input(Fore.RESET+"\n[+]")
        if(intp=="exit"):
            print("[-]Proceso fializado")
            break
        Download(intp)
if __name__ == '__main__':
    main()