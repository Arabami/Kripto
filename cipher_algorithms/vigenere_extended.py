def generate_key_stream(data, key):
    key = key.encode('latin1')  # encode ke bytes
    key_stream = key
    while len(key_stream) < len(data):
        key_stream += key_stream
    return key_stream[:len(data)]

def encrypt(plain_data, key):
    # plain_data: bytes
    key_stream = generate_key_stream(plain_data, key)
    cipher_data = bytes([(plain_data[i] + key_stream[i]) % 256 for i in range(len(plain_data))])
    return cipher_data

def decrypt(cipher_data, key):
    # cipher_data: bytes
    key_stream = generate_key_stream(cipher_data, key)
    plain_data = bytes([(cipher_data[i] - key_stream[i]) % 256 for i in range(len(cipher_data))])
    return plain_data
