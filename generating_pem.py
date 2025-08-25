import rsa

public_key, private_key = rsa.newkeys(2048)

with open("my_private_key.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))
with open("my_public_key.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

message = input("Please write the message you want to cipher (maximum 245 bytes): ")
encrypted = rsa.encrypt(message.encode("utf-8"), public_key)
with open("encrypted_message.bin", "wb") as f:
    f.write(encrypted)

print("You succesfully generated 'encrypted_message.bin'.")