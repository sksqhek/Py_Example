import socket, pickle

port = 2500
maxsize = 1024

sock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)  # UDP 소켓
sock.bind(('', port))

print("수신 대기 중")

while True:
    data, addr = sock.recvfrom(maxsize)
    print("Received message: ", data.decode('utf-8'), addr)

    sock.sendto(("Echo "+ data.decode('utf-8')).encode(),addr)

