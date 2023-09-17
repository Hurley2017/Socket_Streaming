import socket
from Additional_Function import Transfer, Reader
from time import sleep

Transfer = Transfer()
Reader = Reader()

SERVER_ADDRESS = input("Enter Server Address : ")
SERVER_PORT = 5000
PACKAGE_BYTE_LENGTH = 4096

Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client_Socket.connect((SERVER_ADDRESS, SERVER_PORT))
Client_Socket.send("SnehoJoggo".encode())

Receipt = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()

if Receipt == "CCReq":
    print("Connection Rejected")
    Client_Socket.close()
    exit()
else:
    Reader.readInstruction()
    User_Response = input("Enter your choice : ")
    if User_Response == "1":
        Client_Socket.send("Download".encode())
        Files = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
        Files = Files.split(',')
        Reader.readFiles(Files)
        while True:
            File_Input = int(input("Enter your choice : "))
            if File_Input <= len(Files) and File_Input > 0:
                FileName = Files[int(File_Input)-1]
                break
            else:
                Reader.readERROR("Invalid Input")
        Client_Socket.send(FileName.encode())
        try:
            Package_Information = Client_Socket.recv(PACKAGE_BYTE_LENGTH).decode()
            Package_Information = Package_Information.split(':')
            Chunks = []
            while True:
                if len(Chunks) == int(Package_Information[0])-1:
                    Chunk = Client_Socket.recv(int(Package_Information[1]), socket.MSG_WAITALL)
                    Chunks.append(Chunk)
                    break
                Chunk = Client_Socket.recv(PACKAGE_BYTE_LENGTH, socket.MSG_WAITALL) 
                Chunks.append(Chunk)
            ByteFile = Transfer.combineByte(Chunks)
            Transfer.saveByte(ByteFile, FileName, "Client")
            FileSize = Transfer.fileSizeinBytes(FileName, "Client")
            print("Received : " + str(FileSize) + " bytes successfully.")
            Client_Socket.close()
        except:
            print("Failed to Receive...")
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
        try:
            FileSize = Transfer.fileSizeinBytes(FileName, "Client")
            ByteFile = Transfer.returnByte(FileName, "Client")
            Chunks = Transfer.splitByte(ByteFile, PACKAGE_BYTE_LENGTH)
            Package_Information = str(len(Chunks)) + ',' + str(len(Chunks[-1]))
            Package_Information = Package_Information.encode()
            Client_Socket.send(Package_Information)
            sleep(1)
            for Chunk in Chunks:
                Client_Socket.send(Chunk)
            print("Sent : " + str(FileSize) + " bytes successfully.")
            Client_Socket.close()
        except:
            print("Failed to Send...")
            Client_Socket.close()
    else:
        Client_Socket.close()