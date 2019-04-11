import socket
#                             网络           tcp
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
phone.bind(("127.0.0.1", 9999))
phone.listen(3)  # 半连接池

while True:
    conn, address = phone.accept()  # 阻塞 等待客户端connect 这个过程是三次握手

    while True:
        try:
            msg = conn.recv(1024).decode()
            print("检测客户端在线发空")
            # mac系统 客户端关闭这里收到空包有报头但是数据是空的,阻塞不住
            # 数据且conn依然存活且recv不阻塞,下面的send也不会检测客户端不会报错,会一直循环，正常客户端发空是阻塞的
            #  但是select模块send处会检测客户端 如果客户关闭会报错
            if not msg:
                break
            print("客户端发来的消息是:%s" % msg)
            conn.send(msg.upper().encode())
        # windows使用客户端关闭 服务端conn失效
        except Exception:
            break
    # conn.close()

phone.close()