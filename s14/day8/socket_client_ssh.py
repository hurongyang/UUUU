__author = "Hu Rongyang"
import socket
client = socket.socket()

client.connect(('localhost',9999))

while True:
    cmd = input("请输入命令：").strip()
    if len(cmd) == 0:
        continue

    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024)#接收命令结果的长度
    print("命令结果大小：",cmd_res_size)

    received_size = 0
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)#每次收到的有可能小于1024，所以必须用len()判断
        #print(data.decode("utf-8"))
        print(received_size)
    else:
        print("cmd res recived done。。。。",received_size)
    #print(cmd_res.decode("utf-8"))


client.close()