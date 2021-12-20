
from pytube import YouTube

link= input("paste the link ")
print("downloading...")

YouTube(link).streams.get_highest_resolution().download()
print("video download sucessfully")