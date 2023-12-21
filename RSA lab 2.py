from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import os

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_data(private_key, data):
    ciphertext = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return ciphertext

def decrypt_data(public_key, ciphertext):
    try:
        public_key.verify(
            ciphertext,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return data
    except InvalidSignature:
        print("Decryption failed. Invalid signature.")
        return None

def write_to_file(filename, content):
    mode = 'wb' if isinstance(content, bytes) else 'w'
    with open(filename, mode) as f:
        f.write(content)



def read_from_file(filename, mode='rb'):
    with open(filename, mode) as f:
        content = f.read()
    return content

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    data = b"Hello Professor Berry.Greetings From Sivatheja Kopparaju"
    ciphertext = encrypt_data(private_key, data)
    write_to_file("ciphertext.bin", ciphertext)
    ciphertext_from_file = read_from_file("ciphertext.bin")
    decrypted_data = decrypt_data(public_key, ciphertext_from_file)
    if decrypted_data:
        write_to_file("decrypted_data.txt", decrypted_data.decode('utf-8'))
