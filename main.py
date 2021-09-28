import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from player.videoplayer import app
from player.videoplayer import call_py
kay = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="player"),
)


kay.start()
app.start()
call_py.start()
idle()
    
