# TCP_sendfile.py
# 파일 전송 프로그램

import socket, os

port = 2500
s_sock = socket.socket()
host = ""
s_sock.bind((host, port))
s_sock.listen(1)

print('Waiting for connection....')

c_sock, addr = s_sock.accept()  # 클라이언트와 연결
print('Connected from', addr)
#준비완료 메시지 송신
c_sock.send("I am ready".encode()) #준비 완료 메시지 송신. 송신 바이트 수 반환
# 파일 이름 수신
fn = c_sock.recv(1024).decode() # 경로를 포함한 파일이름 수신
filename = os.path.basename(fn) # 기본 파일이름 추출

# 파일을 생성하고 수신 내용을 저장한다
w_file = 'C:/Temp/테스트파일/'+ filename
with open(w_file, 'wb') as f: #저장 파일 열기
    print('file opened')
    print('receiving file...')
    while True:
        data = c_sock.recv(8192) #파일 내용 수신
        if not data: #내용이 없으면 종료
            break
        f.write(data)#내용을 파일에 쓰기

print(f'Download complete in {w_file}')

c_sock.close()