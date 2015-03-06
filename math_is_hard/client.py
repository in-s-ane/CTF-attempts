import random, socket, time

IP = "104.131.107.153"
PORT = 12121

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect((IP , PORT))
sock.recv(1024)
for i in range(0 , 20):
    data = sock.recv(1024)
    print data
    dataList = data.split(" ")
    for i in range(0 , 8):
        dataList.pop(0)
    s = ""
    for op in dataList:
        s += op
    i = eval(s)
    print i
    sock.send(str(i))
    
sock.close()
