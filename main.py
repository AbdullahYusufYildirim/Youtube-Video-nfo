from pytubefix import YouTube


url = input("Enter YouTube video URL:")


yt = YouTube(url)

print(f"Title: {yt.title}")
print(f"URL: {url}")
print(f"Duration: {yt.length} seconds")
print(f"Channel: {yt.author}")
print(f"Views: {yt.views}")
print(f"Thumbnail Url : {yt.thumbnail_url}")