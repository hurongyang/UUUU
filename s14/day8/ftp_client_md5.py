__author = "Hu Rongyang"
import socket
import hashlib
client = socket.socket()
client.connect(('localhost',9999))

while True:
    cmd = input("请输入ftp命令:").strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith("get"):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print("server response：",server_response)
        client.send(b"ready to recv file")
        file_total_size = int(server_response.decode())
        filename = cmd.split()[1]

        received_size = 0
        f = open(filename+".new","wb")
        m = hashlib.md5()
        while received_size < file_total_size:
            if file_total_size - received_size > 1024:   #要收不止一次
                size = 1024
            else:
                size = file_total_size - received_size
                print("last receive：",size)
            data = client.recv(size)
            received_size += len(data)
            m.update(data)
            f.write(data)
        else:
            client_file_md5 = m.hexdigest()
            print("file recv done...........",received_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print("server file md5：",server_file_md5.decode())
        print("client file md5：",client_file_md5)

client.close()