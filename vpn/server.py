import socket
from .crypto import encrypt, decrypt, generate_key
from .protocol import unpack_message, pack_message

def start_server(host, port, key):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"VPN Server listening on {host}:{port}")
    while True:
        conn, addr = s.accept()
        print(f"Client connected: {addr}")
        handle_client(conn, key)

def handle_client(conn, key):
    while True:
        enc_message = unpack_message(conn)
        if enc_message is None:
            break
        message = decrypt(key, enc_message)
        print("Received:", message)
        # Echo back (for now, for demo)
        conn.sendall(pack_message(encrypt(key, message)))
    conn.close()
