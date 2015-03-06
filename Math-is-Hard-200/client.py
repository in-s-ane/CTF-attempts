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
        token = token[1:].strip() # gets rid of the colon matched in regex
        ops = token.split(" ")
        #print ops
        first_num = int(ops[0])
        operation = ops[1]
        second_num = int(ops[2])
        result = first_num + second_num
        # result = eval(token) # we use protection
        sock.sendall(str(result))
    received = sock.recv(1024)

received = sock.recv(1024)
received = received.split("\n")
equations = received[1:-2]
#print equations
i = 0
while i < len(equations):
    equations[i] = equations[i].split(" ")
    i += 1
x0_cof = int(equations[0][0][:-1])
y0_cof = int(equations[0][2][:-1])
sum0 = int(equations[0][4])
x1_cof = int(equations[1][0][:-1])
y1_cof = int(equations[1][2][:-1])
sum1 = int(equations[1][4])
mult = y0_cof * 1.0 / y1_cof
x1_cof *= mult
y1_cof *= mult
sum1 *= mult
x0_cof -= x1_cof
sum0 -= sum1
value_of_x = int(sum0 / x0_cof)
value_of_y = int((sum1 - x1_cof * value_of_x) / y1_cof)
#print value_of_x, value_of_y
sock.sendall(str(value_of_x))
received = sock.recv(1024) # asks for the value of y
sock.sendall(str(value_of_y))

received = sock.recv(1024)
while received.find("calculate the derivative of the following equation") == -1:
    print received
    received = sock.recv(1024)
    if received == "":
        received = sock.recv(1024)
    equations = received.split("\n")
    equations = equations[:-2]
    print equations
    i = 0
    while i < len(equations):
        equations[i] = equations[i].split(" ")
        i += 1
    x0_cof = int(equations[0][0][:-1])
    y0_cof = int(equations[0][2][:-1])
    sum0 = int(equations[0][4])
    x1_cof = int(equations[1][0][:-1])
    y1_cof = int(equations[1][2][:-1])
    sum1 = int(equations[1][4])
    mult = y0_cof * 1.0 / y1_cof
    x1_cof *= mult
    y1_cof *= mult
    sum1 *= mult
    x0_cof -= x1_cof
    sum0 -= sum1
    value_of_x = int(sum0 / x0_cof)
    value_of_y = int((sum1 - x1_cof * value_of_x) / y1_cof)
    print value_of_x, value_of_y
    sock.sendall(str(value_of_x))
    received = sock.recv(1024) # asks for the value of y
    sock.sendall(str(value_of_y))
    received = sock.recv(1024)
