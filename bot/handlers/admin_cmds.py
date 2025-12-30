from bot.core.admin import is_owner

async def admin_cmd(client, message):
    if not is_owner(message.from_user.id):
        return
    await message.reply("Admin command received.")
