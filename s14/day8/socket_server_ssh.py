__author = "Hu Rongyang"
import socket,os
server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令。。。。")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        print("执行指令：",data.decode())
        cmd_res = os.popen(data.decode()).read()#执行命令
        print("before send:",len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = "cmd has no output....."
        conn.send( str(len(cmd_res.encode())).encode("utf-8") )#先发大小给客户端
        conn.send(cmd_res.encode("utf-8"))#发送执行结果
        print("send done")
server.close()