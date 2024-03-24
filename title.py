from pytube import YouTube

def get_title(link):
     
    yt = YouTube(link)

    return yt.title
