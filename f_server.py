import socket
import threading
from Additional_Function import Transfer, Reader
SERVER_ADDRESS = '127.0.0.1' 
SERVER_PORT = 40000

Transfer = Transfer()
Reader = Reader()

Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Server_Socket.bind((SERVER_ADDRESS, SERVER_PORT))


def Process(Client_Address, Client_Port):
    Client_Address = (Client_Address, Client_Port)
    Musics = Transfer.listFile("Music")
    Server_Socket.sendto(Musics.encode(), Client_Address)
    FileName, Client_Address = Server_Socket.recvfrom(2048)
    FileName = FileName.decode()
    print(FileName)
    FileByte = Transfer.returnByte(FileName, "Music")
    Chunks = Transfer.splitByte(FileByte, 65536)
    for Chunk in Chunks:
        Server_Socket.sendto(Chunk, Client_Address)
        break
    for Chunk in Chunks[1:]:
        print("Sending : " + FileName + " to " + str(Client_Address) + " ..." )
        Server_Socket.sendto(Chunk, Client_Address)
while True:
    Client_Message, Client_Address = Server_Socket.recvfrom(2048)
    print(Client_Address)
    Client_Message = Client_Message.decode()
    if Client_Message == "SnehoJoggo":
        Server_Socket.sendto("Hello".encode(), Client_Address)
        threading.Thread(target=Process, args=(Client_Address[0], Client_Address[1])).start()
    else:
        Server_Socket.sendto("CCReq".encode(), Client_Address)
        

