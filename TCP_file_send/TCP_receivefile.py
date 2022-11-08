#TCP_receivefile.py
# 파일 수신 프로그램

import socket, os

s_sock = socket.socket()
host = socket.gethostname()
ip_addr = socket.gethostbyname(host)
port = 2500

s_sock.connect((ip_addr, port)) #서버와 연결

# 상대방의 준비완료를 기다린다
msg = s_sock.recv(1024)  # 클라이언트로부터 준비 완료 수신
print(msg.decode())
# 경로를 포함한 파일 이름을 입력
filename = input('File name to send(c:/test/sample.bin): ')  # ''/' 사용하여 경로 구분
print(f"Sending '{filename}'")
s_sock.sendall(filename.encode())  # 파일 이름 전송
# 파일을 읽기 모드로 열고 sendfile() 함수로 파일 내용 전송
with open(filename, 'rb') as f:
    s_sock.sendfile(f, 0)  # 파일 내용 전송

    # 파일 내용을 읽어 read() 함수로 전송할 수도 있다
    # data = f.read()
    # while data:
    #    c_sock.sendall(data)
    #    data = f.read()

print('Sending complete')

s_sock.close()
print('Connection closed')