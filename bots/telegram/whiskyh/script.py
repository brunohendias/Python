from setup import app
from utils import commands
from logger import log, error

@app.on_message()
async def message(cliente, msg):
    try:
        lower = msg.text.lower()
        if "youtu.be" in lower or "www.youtube.com" in lower:
            lower = 'youtube'
        elif "instagram.com" in lower:
            lower = 'instagram'
        
        for commmand in commands:
            if commmand.command == lower:
                log(msg.chat.first_name, msg.text)
                return await commmand.action(msg)
            
        return await msg.reply(msg.text)
    except Exception as err:
        error(err, msg.chat.first_name, msg.text)

app.run()