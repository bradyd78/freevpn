import socket
from .crypto import encrypt, decrypt
from .protocol import pack_message, unpack_message

def connect_vpn(server_ip, server_port, key):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    try:
        while True:
            msg = input("Send: ").encode()
            s.sendall(pack_message(encrypt(key, msg)))
            enc_reply = unpack_message(s)
            if enc_reply is None: break
            reply = decrypt(key, enc_reply)
            print("Server:", reply)
    finally:
        s.close()
