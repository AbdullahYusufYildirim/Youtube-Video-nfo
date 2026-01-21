from pytubefix import YouTube


url = input("Enter YouTube video URL: ")

yt = YouTube(url)

print(f"Title: {yt.title}")

