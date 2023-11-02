import socket

def main():
    try:
        while True:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('localhost', 6666))
            server_socket.listen(1)
            print("Server is listening on port no. 6666!")
            connection, address = server_socket.accept()
            print("Client connected!")

            input_reader = connection.makefile('r')
            output_writer = connection.makefile('w')

            while True:
                client_message = input_reader.readline()
                if not client_message:
                    break
                print("Client: " + client_message, end="")
                server_message = input("Server: ")
                output_writer.write(server_message + "\n")
                output_writer.flush()

            connection.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
