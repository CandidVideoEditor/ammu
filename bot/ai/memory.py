from bot.utils.db import users

def save_user(uid, name, lang):
    users.update_one(
        {"user_id": uid},
        {"$set": {"name": name, "lang": lang}},
        upsert=True
    )

def get_user(uid):
    return users.find_one({"user_id": uid})
