import rsa

def load_private_key(private_key_location):
    with open(private_key_location, "rb") as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read(), format = 'PEM')
    return private_key

def rsa_decrypt(encrypted_data, private_key):
    decrypted = rsa.decrypt(
        encrypted_data, private_key).decode('utf-8')
    return decrypted

def run():
    private_key_location = input("Enter the private key location: ")
    private_key = load_private_key(private_key_location)
    encrypted_file_location = input('Enter the location of the encrypted file: ')
    with open(encrypted_file_location, "rb") as file:
        encrypted_data = file.read()
        decrypted_data = rsa_decrypt(
            encrypted_data, private_key
        )
        print(f"The decrypted message is: {decrypted_data}")

if __name__ == '__main__':
    run()



