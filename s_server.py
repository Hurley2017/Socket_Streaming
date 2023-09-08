import socket
import threading
from Additional_Function import Transfer, Reader

Transfer = Transfer()
Reader = Reader()

SERVER_ADDRESS = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5000

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server_Socket.bind((SERVER_ADDRESS, SERVER_PORT))
Server_Socket.listen(1)
print("Server is ready and listening for Clients...")

def Process(Client_Socket, Client_Address):
    print("Connection Established with " + str(Client_Address))
    Greet = Client_Socket.recv(1024).decode()
    if Greet == "SnehoJoggo":
        Client_Socket.send("Hello from Server".encode())
        Receipt = Client_Socket.recv(1024).decode()
        if Receipt == "Download":
            try:
                Files = Transfer.listFile('Server')
                Client_Socket.send(Files.encode())
                FileName = Client_Socket.recv(1024).decode()
                FileSize = Transfer.fileSizeinBytes(FileName, "Server")
                ByteFile = Transfer.returnByte(FileName, "Server")
                Chunks = Transfer.splitByte(ByteFile, 65536)
                print("Sending : " + FileName + " to " + str(Client_Address) + " ...")
                for Chunk in Chunks:
                    Client_Socket.send(Chunk)
                Client_Socket.send("EOF".encode())
                print(str(FileSize) + " bytes sent")
            except:
                print("Failed to send...")
        elif Receipt == "Upload":
            FileName = Client_Socket.recv(1024).decode()
            Chunks = []
            print("Receiving : " + FileName + " to " + str(Client_Address) + " ...")
            try:
                while True:
                    Hello = Client_Socket.recv(65536)
                    if len(Hello) == 0:
                        break
                    Chunks.append(Hello)
                ByteFile = Transfer.combineByte(Chunks)
                Transfer.saveByte(ByteFile, FileName, "Server")
                FileSize = Transfer.fileSizeinBytes(FileName, "Server")
                print(str(FileSize) + " bytes received")
            except:
                print("Failed to Receive...")
            
    else:
        Client_Socket.send("CCReq".encode())


while True:
    Client_Socket, Client_Address = Server_Socket.accept()
    threading.Thread(target=Process, args=(Client_Socket, Client_Address)).start()
Server_Socket.close()






