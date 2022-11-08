import socket, pickle

BUFFSIZE = 1024
port = 2500
sock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)

msg = "Hello UDP server"
sock.sendto(msg.encode() ,('localhost', port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print("Server says:", data.decode())
    msg = input('Sending message: ')
    sock.sendto(msg.encode() ,addr)

