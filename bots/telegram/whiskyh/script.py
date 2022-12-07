from setup import app
from utils import commands
from logger import log, error
from pytube import YouTube as yt

async def downloadYoutubeVideo(link, msg):
    streams = yt(link).streams.order_by('resolution').filter(file_extension='mp4',progressive="True")
    filename = f"{msg.chat.id}_video.mp4"
    streams[len(streams) - 1].download(filename=filename)
    return await app.send_video(msg.chat.id, filename)

@app.on_message()
async def message(cliente, msg):
    try:
        lower = msg.text.lower()
        resp = msg.text
        
        if 'https://youtu' or 'https://www.youtube.com' in lower:
            log(msg.chat.first_name, msg.text, resp)
            return await downloadYoutubeVideo(resp, msg)

        for command in commands:
            if command.command == lower:
                resp = command.action()
                break
        log(msg.chat.first_name, msg.text, resp)
        await msg.reply(resp)
    except Exception as err:
        error(err, msg.chat.first_name, msg.text, resp)

app.run()