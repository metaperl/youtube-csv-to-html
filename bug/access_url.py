from pytube import YouTube

URL = 'https://youtube.com/watch?v=yiX5KmZ_ojA'

y = YouTube(URL)
print(y.title)