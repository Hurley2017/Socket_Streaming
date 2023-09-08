import socket
import Additional_Function as AF

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5000

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server_Socket.bind((SERVER_ADDRESS, SERVER_PORT))

Server_Socket.listen(1)

Client_Socket, Client_Address = Server_Socket.accept()

Filename = Client_Socket.recv(1024).decode()

FileSize = AF.fileSizeinBytes(Filename)
ByteFile = AF.returnByte(Filename)

Chunks = AF.splitByte(ByteFile, 65536)

for chunk in Chunks:
    Client_Socket.send(chunk)
    print("Sent: " + str(len(chunk)) + " bytes")
Client_Socket.send("EOF".encode())

Server_Socket.close()