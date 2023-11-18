import hashlib

def encrypt_message():
    message = input("Enter the message to encrypt: ")

    sha256_hash = hashlib.sha256(message.encode()).hexdigest()
    sha512_hash = hashlib.sha512(message.encode()).hexdigest()
    sha3_hash = hashlib.sha3_256(message.encode()).hexdigest()

    print(f"SHA256 encrypted message: {sha256_hash}")
    print(f"SHA512 encrypted message: {sha512_hash}")
    print(f"SHA3 encrypted message: {sha3_hash}")

encrypt_message()
