from os import getenv, mkdir
from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()

ADMINS = getenv('ADMINS').split()
DL_FOLDER = getenv('DOWNLOAD_FOLDER', '/data')

mkdir(DL_FOLDER)
app = Client(
    name=__name__,
    api_id=int(getenv('TELEGRAM_API_ID')),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('BOT_TOKEN')
)
