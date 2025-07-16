import argparse
import yaml
import os
from vpn.server import start_server
from vpn.client import connect_vpn
from vpn.crypto import generate_key

def main():
    parser = argparse.ArgumentParser(description="FreeVPN")
    parser.add_argument('mode', choices=['server', 'client'])
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--key', help="32-byte hex key")
    args = parser.parse_args()

    key = bytes.fromhex(args.key) if args.key else generate_key()
    print(f"Using key: {key.hex()}")

    if args.mode == 'server':
        start_server(args.host, args.port, key)
    elif args.mode == 'client':
        connect_vpn(args.host, args.port, key)

if __name__ == "__main__":
    main()
