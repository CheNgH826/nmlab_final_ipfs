import socket
HOST = '140.112.245.175'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    cmd = input("Please input msg: ")
    #clientSocket.sendto(message.encode(),(serverName, serverPort))
    s.send(cmd.encode())
    data = s.recv(1024)
    print(data.decode())

    #s.close()
