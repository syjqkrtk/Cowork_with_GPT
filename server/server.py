import socket
import psutil  # pip install psutil
import time

HOST = ''  # blank means it will listen to any available IP address
PORT = 12345  # choose a port number

# Get the CPU usage percentage
def get_cpu_usage():
    return psutil.cpu_percent()

# Create a server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the HOST and PORT
    server_socket.bind((HOST, PORT))
    # Listen for connections
    server_socket.listen()
    print(f"Server is listening on port {PORT}...")
    try:
        while True:
            # Accept a connection from a client
            client_socket, address = server_socket.accept()
            print(f"Connected by {address}")
            # Keep sending the CPU usage percentage to the client until the connection is closed
            while True:
                # Get the CPU usage percentage
                cpu_usage = get_cpu_usage()
                # Send the CPU usage percentage to the client
                print(cpu_usage)
                try:
                    client_socket.sendall(str(cpu_usage).encode())
                except ConnectionResetError:
                    print("Client closed the connection")
                    break
                # Sleep for 1 second before getting the next CPU usage percentage
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")