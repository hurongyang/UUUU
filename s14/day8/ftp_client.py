__author = "Hu Rongyang"
import socket
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
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            f.write(data)
            #print(file_total_size,received_size)
        else:
            print("file recv done...........",received_size,file_total_size)
            f.close()

client.close()