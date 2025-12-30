from bot.database.mongo import users

def save_user(uid, name, lang):
    users.update_one(
        {"user_id": uid},
        {"$set": {"name": name, "lang": lang}},
        upsert=True
    )
