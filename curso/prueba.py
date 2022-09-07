
from pytube import YouTube

url = input("Introduce la URL del video: ")
y=YouTube(url)
y.streams.get_highest_resolution().download()
y.streams.get_audio_only().download()
print("Descarga completada", y.title)