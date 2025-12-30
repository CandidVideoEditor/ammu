from pyrogram import filters

async def welcome(client, message):
    for user in message.new_chat_members:
        await message.reply(
            f"Hey {user.first_name} 😄\n"
            "Welcome to *Karunadu Kings Kingdom* 👑\n"
            "Respect • Friendship • Positivity 💛",
            parse_mode="markdown"
        )
