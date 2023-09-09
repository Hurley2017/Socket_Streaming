import socket
from Additional_Function  import Transfer, Reader
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

Transfer = Transfer()
Reader = Reader()  

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 40000
ADDRESS = (SERVER_ADDRESS, SERVER_PORT)

Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Client_Socket.sendto("SnehoJoggo".encode(), ADDRESS)

Server_Message, Server_Address = Client_Socket.recvfrom(2048)
Server_Message = Server_Message.decode()

if Server_Message == "CCreq":
    Client_Socket.close()
else:
    Musics, Server_Address = Client_Socket.recvfrom(2048)
    Musics = Musics.decode().split(",")
    Reader.readFiles(Musics)
    while True:
        File_Input = int(input("Enter your choice : "))
        if File_Input <= len(Musics) and File_Input > 0:
            FileName = Musics[File_Input-1]
            break
        else:
            Reader.readERROR("Invalid Input")
    Client_Socket.sendto(FileName.encode(), ADDRESS)
    FMTHeader, Server_Address = Client_Socket.recvfrom(44)
    while True:
        Chunk = Client_Socket.recvfrom(65536)[0]
        if len(Chunk) == 0:
            break
        else:
            print("got")
            Chunk = Transfer.combineByte([FMTHeader, Chunk])
            soundChunk = AudioSegment(Chunk, format='mp3')
            play(soundChunk)
    Client_Socket.close()
        
