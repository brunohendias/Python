from os import getenv
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

app = Client(
    'whiskyh_bot',
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_API_TOKEN')
)