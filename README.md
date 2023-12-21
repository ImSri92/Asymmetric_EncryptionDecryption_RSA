# Asymmetric_EncryptionDecryption_RSA
Asymmetric Encryption and Decryption with RSA in Python
Key Pair Generation:

generate_key_pair(): Generates an RSA private-public key pair with a specified public exponent and key size.
Encryption and Decryption Functions:

encrypt_data(private_key, data): Encrypts data using the private key, producing a signature utilizing PSS padding and SHA256 hashing.
decrypt_data(public_key, ciphertext): Decrypts the ciphertext using the public key. It verifies the signature using PSS padding and SHA256 hashing. If the signature is valid, returns the decrypted data.

File I/O Functions:
write_to_file(filename, content): Writes content to a file, considering whether it's binary data or text.
read_from_file(filename, mode='rb'): Reads content from a file, adjusting the mode for binary or text reading.

Main Execution:
Generates a new RSA key pair.
Defines a sample data to be encrypted.
Encrypts the data using the private key and saves the ciphertext to a file named "ciphertext.bin".
Reads the ciphertext from the file.
Decrypts the ciphertext using the public key. If successful, writes the decrypted data to a file named "decrypted_data.txt".

This code demonstrates the usage of the RSA algorithm for asymmetric encryption and decryption in Python, showcasing the process of generating key pairs, encrypting data with a private key, and subsequently decrypting it with the corresponding public key.
