def generate_key(text, key):
    key = key.upper()
    key_index = 0
    full_key = ""

    for char in text:
        if char.isalpha():
            full_key += key[key_index % len(key)]
            key_index += 1

    return full_key

def preprocess_text(text):
    # Hilangkan semua karakter non-alfabet
    return ''.join([char for char in text if char.isalpha()])

def encrypt(text, key):
    text = preprocess_text(text)
    key = generate_key(text, key)
    result = []

    for t_char, k_char in zip(text, key):
        base = ord('A') if t_char.isupper() else ord('a')
        shift = ord(k_char.upper()) - ord('A')
        enc_char = chr((ord(t_char.upper()) - ord('A') + shift) % 26 + ord('A'))
        result.append(enc_char)

    return ''.join(result)

def decrypt(text, key):
    text = preprocess_text(text)
    key = generate_key(text, key)
    result = []

    for t_char, k_char in zip(text, key):
        base = ord('A') if t_char.isupper() else ord('a')
        shift = ord(k_char.upper()) - ord('A')
        dec_char = chr((ord(t_char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
        result.append(dec_char)

    return ''.join(result)
