from os import popen
from Models.Command import Command
from bs4 import BeautifulSoup as bs
from requests import get
from pytube import YouTube as yt
from setup import app

def SOCommand(command: str):
    return popen(command).read()

def removeImage():
    SOCommand('rm *.jpg')

def removeVideo():
    SOCommand('rm *.mp4')

def DownloadImage(link):
    SOCommand(f"curl '{link}' >> post.jpg")
    
async def randomPassword(msg):
    password = SOCommand('openssl rand -base64 50')
    return await msg.reply(password)

async def downloadYoutubeVideo(msg):
    removeVideo()
    streams = yt(msg.text).streams.order_by('resolution').filter(file_extension='mp4',progressive="True")
    filename = f"{msg.chat.id}_video.mp4"
    streams[len(streams) - 1].download(filename=filename)
    return await app.send_video(msg.chat.id, filename)

async def downloadInstagramImagePost(msg):
    removeImage()
    post = get(msg.text)
    soup = bs(post.text, 'html.parser')
    metas = soup.find_all('meta')
    for meta in metas:
        try:
            if 'image' in meta.attrs['name']:
                DownloadImage(meta.attrs['content'])
                return await app.send_photo(msg.chat.id, 'post.jpg')
        except:
            pass

commands = [
    Command('password', randomPassword),
    Command('youtube', downloadYoutubeVideo),
    Command('instagram', downloadInstagramImagePost)
]