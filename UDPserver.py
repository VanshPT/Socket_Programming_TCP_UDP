import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 6666))
    print("Server is listening on port no. 6666!")

    while True:
        client_message, client_address = server_socket.recvfrom(1024)
        print(f"Client {client_address}: {client_message.decode()}")

        server_message = input("Server: ")
        server_socket.sendto(server_message.encode(), client_address)

if __name__ == "__main__":
    main()
