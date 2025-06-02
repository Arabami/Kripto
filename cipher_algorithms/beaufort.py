def format_text(text):
    return ''.join(filter(str.isalpha, text.upper()))

def extend_key(text, key):
    key = key.upper()
    key = ''.join(filter(str.isalpha, key))
    return (key * (len(text) // len(key))) + key[:len(text) % len(key)]

def encrypt(plaintext, key):
    plaintext = format_text(plaintext)
    key = extend_key(plaintext, key)
    ciphertext = ""

    for p, k in zip(plaintext, key):
        c = (ord(k) - ord(p)) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

def decrypt(ciphertext, key):
    # Beaufort Cipher is reciprocal: decrypt == encrypt
    return encrypt(ciphertext, key)