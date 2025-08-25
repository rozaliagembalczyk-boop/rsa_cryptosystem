# rsa_cryptosystem
This project is a Python-based tool that demonstrates asymmetric cryptography using the RSA algorithm. The script allows users to securely decrypt messages that were encrypted with a public RSA key. It covers the full workflow of RSA cryptography, including key management, encryption, and decryption.

Key Features:

Private Key Loading: Reads RSA private keys from PEM files to ensure secure decryption.

Encrypted File Support: Reads encrypted messages from binary files (.bin) for flexible input.

Decryption Functionality: Decrypts messages and displays both the encrypted (raw) and decrypted content.

Error Handling: Alerts users if decryption fails due to incorrect keys or corrupted data.

Optional Output to File: Can save the decrypted message to a separate .txt file for further use.
