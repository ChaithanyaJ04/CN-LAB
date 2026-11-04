import socket

serverName = "127.0.0.1"
serverPort = 12530

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName , serverPort))

filename=input("Enter the file name:")
clientSocket.send(filename.encode())

filecontents=clientSocket.rec(1024).decode()
print("From server: ",filecontents)

clientSocket.close()