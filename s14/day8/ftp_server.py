__author = "Hu Rongyang"
import hashlib
import socket,os,time
server = socket.socket()
server.bind(('localhost',9999))

server.listen()

while True:
    conn,addr = server.accept()
    print("new xonn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已经断开")
            break
        cmd,filename = data.decode().split()
        print(filename)
        if os.path.isfile(filename):
            f = open(filename,"rb")
            #m = hashlib.md5()
            file_size = os.stat(filename).st_size  #通过os模块获取文件大小
            conn.send(str(file_size).encode())     #send file size
            conn.recv(1024)                        #wait for ack
            for line in f:
                #m.update(line)
                conn.send(line)
            #print("file md5:",m.hexdigest())
            f.close()

        print("send done")

server.close()