from vpn.client import connect_vpn

if __name__ == "__main__":
    server_ip = input("Enter VPN server IP: ")
    server_port = int(input("Enter VPN server port: "))
    connect_vpn(server_ip, server_port)
