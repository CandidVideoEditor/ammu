def is_text_allowed(text):
    bad_words = ["spam", "abuse"]
    return not any(word in text.lower() for word in bad_words)
