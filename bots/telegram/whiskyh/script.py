from setup import app
from utils import commands
from logger import log, error

@app.on_message()
async def message(cliente, msg):
    try:
        lower = msg.text.lower()
        resp = msg.text
        for command in commands:
            if command.command == lower:
                resp = command.action()
                break
        log(msg.chat.first_name, msg.text, resp)
        await msg.reply(resp)
    except Exception as err:
        error(err, msg.chat.first_name, msg.text, resp)

app.run()