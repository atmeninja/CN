# TCP Client
import socket

def tcp_client():
    # Create a socket and connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 4000))

    # Get the filename from the user
    fname = input("Enter the filename: ")

    # Send the filename to the server
    sock.sendall(fname.encode())

    # Receive and print the file content from the server
    print("\nReceived file content:")
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(data.decode(), end="")

    sock.close()

if __name__ == "__main__":
    tcp_client()
