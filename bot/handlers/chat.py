from bot.ai.language_detect import detect_language
from bot.ai.response_engine import generate_reply
from bot.ai.memory_brain import save_user

async def chat_handler(client, message):
    user = message.from_user
    lang = detect_language(message.text)
    save_user(user.id, user.first_name, lang)
    reply = generate_reply(user.first_name, lang)
    await message.reply_text(reply)
