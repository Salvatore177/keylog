# keylog


Disclaimer: 
Questo software è stato sviluppato per scopi didattici e di sicurezza informatica. È responsabilità dell'utente assicurarsi di utilizzarlo nel rispetto delle leggi e delle normative locali.

# AES-Based Secure Keylogger

Questo progetto implementa un keylogger con funzionalità di crittografia AES per proteggere i dati trasmessi a un server remoto. È stato progettato a scopo educativo e deve essere utilizzato esclusivamente in ambienti controllati e con il consenso esplicito di tutte le parti coinvolte.

---

## **Caratteristiche**

- **Crittografia AES (CBC Mode)**: I dati, inclusi gli indirizzi IP e i tasti, sono crittografati utilizzando AES con padding.
- **Gestione dinamica delle chiavi**: La chiave AES viene caricata da variabili d'ambiente per una maggiore sicurezza.
- **Funzionalità keylogger**: Rileva e invia i tasti premuti al server remoto.

---

## **Prerequisiti**

- **Python 3.7+**
- Librerie Python:
  - `pynput`
  - `pycryptodome`
- **Un server TCP** configurato per ricevere connessioni sulla porta specificata.

---

## **Come utilizzare**

### **1. Configurazione del progetto**
1. Clona il repository:
    ```bash
    git clone <URL_DEL_REPOSITORY>
    cd <NOME_CARTELLA>
    ```
2. Installa le dipendenze:
    ```bash
    pip install pynput pycryptodome
    ```

3. Configura la chiave AES:
    - Genera una chiave AES casuale:
        ```python
        from Crypto.Random import get_random_bytes
        print(get_random_bytes(16).hex())
        ```
    - Esporta la chiave come variabile d'ambiente:
        ```bash
        export AES_KEY=<CHIAVE_GENERATA>
        ```

4. Configura l'indirizzo IP crittografato:
    - Modifica il valore di `encrypted_ip` nel codice:
        ```python
        encrypted_ip = "<VALORE_CIFRATO>"
        ```

### **2. Avvio del keylogger**
- Avvia lo script principale:
    ```bash
    python keylogger.py
    ```

### **3. Server TCP**
Assicurati che il server TCP sia in ascolto sulla porta specificata (di default: 8080).

---

## **Avvertenze**

- **Uso responsabile**: Questo progetto è esclusivamente per scopi educativi. L'utilizzo non autorizzato è una violazione della legge.
- **Sicurezza**: Non condividere la tua chiave AES o l'IP crittografato.
- **Ambiente controllato**: Testa e utilizza il progetto solo in un ambiente di laboratorio con permessi appropriati.

---

## **Funzioni principali**

### **Crittografia AES**
- **encrypt_aes_cbc(key, data)**: Crittografa i dati utilizzando AES in modalità CBC.
- **decrypt_aes_cbc(key, encrypted_data)**: Decrittografa i dati crittografati.

### **Keylogger**
- **handle_keys(key)**: Gestisce la pressione dei tasti e invia i dati crittografati al server.
- **start_keylogger(server_port)**: Avvia il keylogger e si connette al server.

---

## **Contributi**

Se desideri contribuire, crea una pull request o apri una issue per discutere le modifiche.

---

## **Licenza**

Questo progetto è rilasciato sotto la licenza [MIT](LICENSE).
