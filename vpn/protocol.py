import struct

# Simple example: [length][data]
def pack_message(data: bytes) -> bytes:
    return struct.pack('!I', len(data)) + data

def unpack_message(sock):
    lengthbuf = sock.recv(4)
    if not lengthbuf:
        return None
    length, = struct.unpack('!I', lengthbuf)
    data = b''
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            return None
        data += chunk
    return data
