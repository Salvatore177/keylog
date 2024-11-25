from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Funzione per aggiungere padding ai dati
def pad(data):
    pad_len = AES.block_size - len(data) % AES.block_size
    return data + bytes([pad_len] * pad_len)

# Funzione per rimuovere il padding
def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

# Crittografia con AES (CBC mode)
def encrypt_aes_cbc(key, data):
    iv = get_random_bytes(16)  # Genera un IV casuale
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data.encode('utf-8'))
    encrypted_bytes = cipher.encrypt(padded_data)
    return base64.b64encode(iv + encrypted_bytes).decode('utf-8')

# Decrittografia con AES (CBC mode)
def decrypt_aes_cbc(key, encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]  # Estrai l'IV
    encrypted_bytes = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes))
    return decrypted_bytes.decode('utf-8')

key = get_random_bytes(16)  # Genera una chiave casuale di 16 byte
print(f"Chiave generata: {key.hex()}")  # Stampa la chiave in formato esadecimale
ip = ""

# Crittografare l'IP
encrypted_ip = encrypt_aes_cbc(key, ip)
print(f"Indirizzo IP crittografato con CBC: {encrypted_ip}")

# Decrittografare l'IP
decrypted_ip = decrypt_aes_cbc(key, encrypted_ip)
print(f"Indirizzo IP decrittografato con CBC: {decrypted_ip}")
