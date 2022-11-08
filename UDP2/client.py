#UDP클라이언트 통신
import pickle
import socket
BUFFSIZE = 1024
port = 2500

#UDP 소켓 생성
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = "Hello UDP server"

#메시지 전송
sock.sendto(msg.encode(),('localhost', port))

#메시지 송수신
while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print("Server says:", data.decode())
    msg = input('Sending message: ')
    #sock.sendto(msg.encode(), addr) #메시지 전송
    T = pickle.dumps(25, 'd')
    sock.sendto(T, addr)  # 메시지 전송