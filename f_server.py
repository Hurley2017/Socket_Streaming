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
        Files = Transfer.listFile('Music')
        Client_Socket.send(Files.encode())
        FileName = Client_Socket.recv(1024).decode()
        FileName = Transfer.any2WAV(FileName, "Music")
        FileSize = Transfer.fileSizeinBytes(FileName, "Music")
        ByteFile = Transfer.returnByte(FileName, "Music")
        Chunks = Transfer.splitByte(ByteFile, 65536)
        print("Sending : " + FileName + " to " + str(Client_Address) + " ...")
        for Chunk in Chunks:
            Client_Socket.send(Chunk)
        Client_Socket.send("EOF".encode())
        print(str(FileSize) + " bytes sent")
        try:
            pass
        except:
            print("Failed to send...")        
    else:
        Client_Socket.send("CCReq".encode())


while True:
    Client_Socket, Client_Address = Server_Socket.accept()
    threading.Thread(target=Process, args=(Client_Socket, Client_Address)).start()
Server_Socket.close()






