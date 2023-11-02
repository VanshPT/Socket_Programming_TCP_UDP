import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 6666)

    while True:
        client_message = input("Client: ")
        client_socket.sendto(client_message.encode(), server_address)

        server_message, server_address = client_socket.recvfrom(1024)
        print(f"Server: {server_message.decode()}")

if __name__ == "__main__":
    main()
