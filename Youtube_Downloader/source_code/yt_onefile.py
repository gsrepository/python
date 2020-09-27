from pytube import YouTube
from pytube.cli import on_progress

file_name = input("Please give the video link here : ")
try:

    ytd = YouTube(file_name,on_progress_callback=on_progress)
    video = ytd.streams.filter(file_extension='mp4').get_highest_resolution()
    video.download()

except EOFError as err:
    print(err)
else:
    print("File downloaded successfully!")