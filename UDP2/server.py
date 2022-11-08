#UDP 서버 프로그램
import pickle
import socket
port = 2500
maxsize = 1024

#UDP 소켓을 생성하고 주소와 포트 결합
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP 소켓
sock.bind(('', port))
print("수신 대기 중")

#데이터를 수신하고 다시 전송한다
while True:
    #데이터 수신
    data, addr = sock.recvfrom(maxsize) #데이터와 상대방 종단점 주소 수신
    print("Received message: ", data.decode())
    print(addr)

    T = pickle.loads(data)
    if T:
        print(T)

    #데이터ㅠ 송신
    sock.sendto(data,addr) #재전송


