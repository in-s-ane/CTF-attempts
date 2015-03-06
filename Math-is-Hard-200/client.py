import sys, socket, re

HOST = "104.131.107.153"
PORT = 12121

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

received = sock.recv(1024)
print received

received = sock.recv(1024)
while received.find("Hey, nice job! Okay, we're done with the addition part, now it's going to get harder:") == -1:
    print received
    parser = re.compile(r': .*$')
    for token in parser.findall(received):
        token = token[2:]
        ops = token.split(" ")
        #print ops
        first_num = int(ops[0])
        operation = ops[1]
        second_num = int(ops[2])
        result = first_num + second_num
        sock.sendall(str(result))
    received = sock.recv(1024)

received = sock.recv(1024)
while True:
    print received
    break
