import socket
import threading
from Additional_Function import Transfer, Reader
from time import sleep

Transfer = Transfer()
Reader = Reader()

SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5000
PACKAGE_BYTE_LENGTH = 4096

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server_Socket.bind((SERVER_ADDRESS, SERVER_PORT))
Server_Socket.listen(1)
print("Server is ready and listening for Clients...")

def Process(Client_Socket, Client_Address):
    print("Connection Established with " + str(Client_Address))
    Greet = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
    if Greet == "SnehoJoggo":
        Client_Socket.send("Hello from Server".encode())
        Receipt = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
        if Receipt == "Download":
            try:
                Files = Transfer.listFile("Server").encode()
                Client_Socket.send(Files)
                FileName = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
                FileSize = Transfer.fileSizeinBytes(FileName, "Server")
                ByteFile = Transfer.returnByte(FileName, "Server")
                Chunks = Transfer.splitByte(ByteFile, PACKAGE_BYTE_LENGTH)
                Package_Information = str(len(Chunks)) + ":" + str(len(Chunks[-1]))
                Package_Information = Package_Information.encode()
                Client_Socket.send(Package_Information)
                sleep(1)
                for Chunk in Chunks:
                    Client_Socket.send(Chunk)
                print("Sent : " + str(FileSize) + " bytes successfully to " + str(Client_Address) + ".")
            except:
                print("Failed to Send...")
        elif Receipt == "Upload":
            try:
                FileName = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
                Package_Information = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
                Package_Information = Package_Information.split(',')
                Chunks = []
                while True:
                    if len(Chunks) == int(Package_Information[0])-1:
                        Chunk = Client_Socket.recv(int(Package_Information[1]))
                        Chunks.append(Chunk)
                        break
                    Chunk = Client_Socket.recv(PACKAGE_BYTE_LENGTH) 
                    Chunks.append(Chunk)
                ByteFile = Transfer.combineByte(Chunks)
                Transfer.saveByte(ByteFile, FileName, "Server")
                print("Received : " + str(FileSize) + " bytes successfully from " + str(Client_Address) + ".")
            except:
                print("Failed to Receive...")
    else:
        Client_Socket.send("CCReq".encode())

while True:
    Client_Socket, Client_Address = Server_Socket.accept()
    threading.Thread(target=Process, args=(Client_Socket, Client_Address)).start()
Server_Socket.close()






