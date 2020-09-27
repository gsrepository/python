from pytube import YouTube
from pytube.cli import on_progress

try:
    f=open("inputfile.txt","r")
    for url in f:
        ytd = YouTube(url,on_progress_callback=on_progress)
        video = ytd.streams.filter(file_extension='mp4').get_highest_resolution()
        video.download()
    f.close()
except EOFError as err:
    print(err)
else:
    print("File downloaded successfully!")
