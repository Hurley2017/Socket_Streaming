import socket
from Additional_Function  import Transfer, Reader
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import sys
sys.path.append('/path/to/ffmpeg')

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
    FMTHeader = Client_Socket.recv(44)
    while True:
        Hello = Client_Socket.recv(65536)
        if len(Hello) == 0:
            break
        else:
            Hello = Transfer.combineByte([FMTHeader, Hello])
            soundChunk = AudioSegment(Hello, format='wav')
            play(soundChunk)
    Client_Socket.close()


