from pytube import YouTube

link= input("paste the link ")
print("downloading...")

YouTube(link).streams.get_audio_only().download()
print("audio download sucessfully")