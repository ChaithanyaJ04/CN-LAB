import socket

serverName = "127.0.0.1"
serverPort = 12530

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName , serverPort))
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    filename = connectionSocket.recv(1024).decode()
    try:
        with open(filename, "r") as file:
            filecontents=file.read(1024)
        connectionSocket.sendall(filecontents.encode())
        print("File contents sent successfully")

    except FileNotFoundError:
        connectionSocket.sendall("File not found".encode())

    finally:
        connectionSocket.close()
    break
serverSocket.close()
print("Server connection closed")
