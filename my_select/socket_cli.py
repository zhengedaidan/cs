import socket

#                             网络           tcp
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(("127.0.0.1", 9999))


while True:
    msg = input("发送内容").strip()
    # if not msg:
    #     continue
        # break
    phone.send(msg.encode())
    print("yifa")
    recv_msg = phone.recv(1024).decode()
    print("服务端回的消息是:{}".format(recv_msg))

phone.close()
print("客户端正常关闭")



