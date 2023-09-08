import socket
from Additional_Function import Transfer, Reader

Transfer = Transfer()
Reader = Reader()

SERVER_ADDRESS = input("Enter Server Address : ")
SERVER_PORT = 5000

Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client_Socket.connect((SERVER_ADDRESS, SERVER_PORT))
Client_Socket.send("SnehoJoggo".encode())

Receipt = Client_Socket.recv(1024).decode()

if Receipt == "CCReq":
    print("Connection Rejected")
    Client_Socket.close()
    exit()
else:
    Reader.readInstruction()
    User_Response = input("Enter your choice : ")
    if User_Response == "1":
        Client_Socket.send("Download".encode())
        Files = Client_Socket.recv(2048).decode()
        Files = Files.split(",")
        Reader.readFiles(Files)
        while True:
            File_Input = int(input("Enter your choice : "))
            if File_Input <= len(Files):
                FileName = Files[int(File_Input)-1]
                break
            else:
                Reader.readERROR("Invalid Input")
        Client_Socket.send(FileName.encode())
        Chunks = []
        while True:
            Hello = Client_Socket.recv(65536)
            if len(Hello) == 0:
                break
            Chunks.append(Hello)
            print("Received: " + str(len(Hello)) + " bytes")
        ByteFile = Transfer.combineByte(Chunks)
        Transfer.saveByte(ByteFile, FileName, "Client")
        Client_Socket.close()
    elif User_Response == '2':
        Client_Socket.send("Upload".encode())
        Files = Transfer.listFile("Client")
        Files = Files.split(",")
        Reader.readFiles(Files)
        while True:
            File_Input = int(input("Enter your choice : "))
            if File_Input <= len(Files):
                FileName = Files[int(File_Input)-1]
                break
            else:
                Reader.readERROR("Invalid Input")
        Client_Socket.send(FileName.encode())
        FileSize = Transfer.fileSizeinBytes(FileName, "Client")
        ByteFile = Transfer.returnByte(FileName, "Client")
        Chunks = Transfer.splitByte(ByteFile, 65536)
        for Chunk in Chunks:
            Client_Socket.send(Chunk)
            print("Sent: " + str(len(Chunk)) + " bytes")
        Client_Socket.send("EOF".encode())
        Client_Socket.close()
    else:
        Client_Socket.close()


