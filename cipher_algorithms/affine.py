def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception(f"Modular inverse for {a} does not exist")
    else:
        return x % m

def encrypt(plain_text, a, b):
    cipher_text = ''
    for char in plain_text.upper():
        if char.isalpha():  # only encrypt letters
            x = ord(char) - ord('A')
            cipher_char = (a * x + b) % 26 + ord('A')
            cipher_text += chr(cipher_char)
    return cipher_text

def decrypt(cipher_text, a, b):
    a_inv = mod_inverse(a, 26)
    plain_text = ''
    for char in cipher_text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            plain_char = a_inv * (x - b) % 26 + ord('A')
            plain_text += chr(plain_char)
    return plain_text
