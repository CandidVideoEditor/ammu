import time
user_time = {}

def is_spam(uid):
    now = time.time()
    if uid in user_time and now - user_time[uid] < 3:
        return True
    user_time[uid] = now
    return False
