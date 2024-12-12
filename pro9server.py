import socket

def tcp_server():
    # Create a socket and bind to the port
    sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sersock.bind(("", 4000))
    sersock.listen(1)

    print("Server ready for connection")
    conn, addr = sersock.accept()
    print("Connection is successful and waiting for requests")

    # Receive the filename from the client
    fname = conn.recv(1024).decode()

    try:
        # Read the file and send its content to the client
        with open(fname, "r") as file:
            for line in file:
                conn.sendall(line.encode())
    except FileNotFoundError:
        conn.sendall(b"File not found.")

    conn.close()
    sersock.close()

if __name__ == "__main__":
    tcp_server()

