import socket
from Additional_Function import Transfer, Reader

Transfer = Transfer()
Reader = Reader()

SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5000

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server_Socket.bind((SERVER_ADDRESS, SERVER_PORT))

Server_Socket.listen(1)

Client_Socket, Client_Address = Server_Socket.accept()

Greet = Client_Socket.recv(1024).decode()

if Greet == "SnehoJoggo":
    Client_Socket.send("Hello from Server".encode())
    Receipt = Client_Socket.recv(1024).decode()
    if Receipt == "Download":
        Files = Transfer.listFile('Server')
        Client_Socket.send(Files.encode())
        FileName = Client_Socket.recv(1024).decode()
        FileSize = Transfer.fileSizeinBytes(FileName, "Server")
        ByteFile = Transfer.returnByte(FileName, "Server")
        Chunks = Transfer.splitByte(ByteFile, 65536)
        for Chunk in Chunks:
            Client_Socket.send(Chunk)
            print("Sent: " + str(len(Chunk)) + " bytes")
        Client_Socket.send("EOF".encode())
        Server_Socket.close()
    else:
        Server_Socket.close()
else:
    Client_Socket.send("CCReq".encode())
    Server_Socket.close()






