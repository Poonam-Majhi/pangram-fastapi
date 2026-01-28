import string

def is_pangram(text: str):
    if text is None:
        text = ""
    alphabet = set(string.ascii_lowercase)
    present = {ch.lower() for ch in text if ch.isalpha()}
    missing = sorted(list(alphabet - present))
    return (len(missing) == 0, missing)