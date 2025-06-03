def encrypt(text, key):
    result = []
    key_digits = [int(k) for k in key]
    key_len = len(key_digits)
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            offset = key_digits[i % key_len]
            new_char = chr((ord(char) - 65 + offset) % 26 + 65)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def decrypt(text, key):
    result = []
    key_digits = [int(k) for k in key]
    key_len = len(key_digits)
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            offset = key_digits[i % key_len]
            new_char = chr((ord(char) - 65 - offset) % 26 + 65)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)