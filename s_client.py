import socket
import Additional_Function as AF

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 5000


Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_Socket.connect((SERVER_ADDRESS, SERVER_PORT))

Filename = 'file12.webm'

Client_Socket.send(Filename.encode())

Chunks = []
while True:
    Hello = Client_Socket.recv(65536)
    if len(Hello) == 0:
        break
    Chunks.append(Hello)
    print("Received: " + str(len(Hello)) + " bytes")


ByteFile = AF.combineByte(Chunks)

AF.saveByte(ByteFile, Filename.split(".")[0]+"copy."+Filename.split(".")[1])

Client_Socket.close()
