import socket

def main():
    try:
        while True:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 6666))
            print("Client is connected to the server!")

            input_reader = client_socket.makefile('r')
            output_writer = client_socket.makefile('w')

            while True:
                client_message = input("Client: ")
                output_writer.write(client_message + "\n")
                output_writer.flush()
                server_message = input_reader.readline()
                if not server_message:
                    break
                print("Server: " + server_message, end="")

            client_socket.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
