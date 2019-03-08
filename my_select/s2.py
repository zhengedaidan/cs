import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(("127.0.0.1", 9000))
print(sk)

while 1:
    msg = input("请输入发送给服务器的消息")
    sk.send(msg.encode())
    data = sk.recv(1024)
    print(data.decode())

