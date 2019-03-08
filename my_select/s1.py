import socket
import select
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

sk.bind(("127.0.0.1",9000))


sk.listen(5)

socket_obj_inputs = [sk,]

while 1:
    print(socket_obj_inputs)
    r,w,e=select.select(socket_obj_inputs,[],[],5) # 3代表3秒一循环
    for socket_obj in r:
        # coon,addr = i.accept()
        # input .append(coon)
        # data = coon.recv(1024)
        if socket_obj == sk:
            conn, addr = socket_obj.accept()
            socket_obj_inputs.append(conn)
        else:
            data = socket_obj.recv(1024)
            print(data,98765)
            import time
            print(data)
            time.sleep(8)
            msg = "回第{}位用户".format(socket_obj_inputs.index(socket_obj))
            socket_obj.sendall(msg.encode())









