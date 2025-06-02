def clean_text(text):
    return ''.join(filter(str.isalpha, text)).upper()

def generate_autokey(text, key):
    key = key.upper()
    if len(key) < len(text):
        key += text[:len(text) - len(key)]
    return key

def encrypt(text, key):
    text = clean_text(text)
    key = generate_autokey(text, key)
    cipher_text = []

    for i in range(len(text)):
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))

    return "".join(cipher_text)

def decrypt(cipher_text, key):
    cipher_text = clean_text(cipher_text)
    key = key.upper()
    orig_text = []

    for i in range(len(cipher_text)):
        if i < len(key):
            current_key = key[i]
        else:
            current_key = orig_text[i - len(key)]

        x = (ord(cipher_text[i]) - ord(current_key) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))

    return "".join(orig_text)
