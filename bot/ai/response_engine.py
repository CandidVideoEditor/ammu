import random

def generate_reply(name, lang):
    responses = {
        "en": [f"Hey {name} 😄", f"How are you {name}?"],
        "kn": [f"{name} 😄 heg iddira?", f"{name} 🤍 chennag iddira?"],
        "ta": [f"{name} 😄 epdi iruka?", f"{name} 🤍 nalla irukiya?"]
    }
    return random.choice(responses.get(lang, responses["en"]))
