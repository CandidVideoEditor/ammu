import asyncio

# FIX: Create event loop for Heroku / Python 3.10+
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters
from bot.utils.config import BOT_TOKEN
from bot.ai.language import detect_lang
from bot.ai.memory import save_user
from bot.ai.reply_engine import reply
from bot.handlers.voice import create_voice
from bot.handlers.welcome import welcome
from bot.handlers.admin import is_owner


app = Client("ammu", bot_token=BOT_TOKEN)


@app.on_message(filters.new_chat_members)
async def on_join(client, message):
    await welcome(client, message)


@app.on_message(filters.text & filters.group)
async def chat(client, message):
    text = message.text
    uid = message.from_user.id
    name = message.from_user.first_name

    lang = detect_lang(text)
    save_user(uid, name, lang)

    if "admin" in text.lower():
        await message.reply("For help, please contact @admins 👑")
        return

    reply_text = reply(name, lang)
    await message.reply_text(reply_text)


@app.on_message(filters.command("voice"))
async def voice(client, message):
    voice = create_voice("Hello! I am Ammu")
    await message.reply_voice(voice)


# 🔥 IMPORTANT: start the bot properly
if __name__ == "__main__":
    app.run()
