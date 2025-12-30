import random

def reply(name, lang):
    if lang == "kn":
        return f"{name} 😄 yen samachara?"
    if lang == "ta":
        return f"{name} 😊 epdi iruka?"
    if lang == "hi":
        return f"{name} 😄 kya haal hai?"
    return f"Hey {name} 😄 how are you?"
