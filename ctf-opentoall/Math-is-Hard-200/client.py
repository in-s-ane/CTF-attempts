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
        first_num = int(ops[0])
        operation = ops[1]
        second_num = int(ops[2])
        result = first_num + second_num
        # result = eval(token) # we use protection 'round here
        sock.sendall(str(result))
    received = sock.recv(1024)

received = sock.recv(1024)
while received.find("calculate the derivative of the following equation") == -1:
    print received
    while received == "":
        received = sock.recv(1024)
        print "Retrying recv"
    equations = received.split("\n")
    equations = equations[1:] # Remove the first line of input
    equations[0] = equations[0].split(" ")
    equations[1] = equations[1].split(" ")
    print "Got Eq 1: " + str(equations[0])
    print "Got Eq 2: " + str(equations[1])
    # Parse equation coefficients
    x0_cof = int(equations[0][0][:-1])
    y0_cof = int(equations[0][2][:-1])
    sum0 = int(equations[0][4])
    x1_cof = int(equations[1][0][:-1])
    y1_cof = int(equations[1][2][:-1])
    sum1 = int(equations[1][4])
    # Do math
    mult = y0_cof * 1.0 / y1_cof
    x1_cof *= mult
    y1_cof *= mult
    sum1 *= mult
    x0_cof -= x1_cof
    sum0 -= sum1
    value_of_x = sum0 / x0_cof
    value_of_y = (sum1 - x1_cof * value_of_x) / y1_cof
    print value_of_x, value_of_y
    sock.sendall(str(value_of_x)[:-2])
    received = sock.recv(1024) # asks for the value of y
    sock.sendall(str(value_of_y)[:-2])
    print "Solved system"
    # Next input comes in two separate lines
    received = sock.recv(1024)
    received += sock.recv(1024)

while received.find("flag") == -1:
    print "Got <<" + received + ">>"
    # Parse value of x
    x = 0
    parser = re.compile(r'x = [0-9]+')
    for token in parser.findall(received):
        x = int(token[4:])
        print "x: " + str(x)
    # Parse function to differentiate
    parser = re.compile(r'f\(x\) = .*')
    x_cof = 0
    x_exp = 0
    terms = []
    for token in parser.findall(received):
        token = token[6:]
        print "Function: " + token
        # Parse the coefficient and exponent of each term of the function
        for term in token.split(" + "):
            term = term.split("x^")
            x_cof = int(term[0])
            if len(term) > 1:
                x_exp = int(term[1])
            else:
                x_exp = 0
            terms.append((x_cof, x_exp))
    # Iterate through terms and perform power rule
    derivative = 0
    for (x_coefficient, x_exponent) in terms:
        print "x coeff: " + str(x_coefficient)
        print "x exp: " + str(x_exponent)
        print "x: " + str(x)
        part = 0
        if x != 0:
            part = int(x_coefficient * x_exponent * (x ** (x_exponent - 1)))
        print str(part)
        derivative += part
    print "Derivative: " + str(derivative)
    sock.sendall(str(derivative))
    # Next input comes in two separate lines
    received = sock.recv(1024)
    received += sock.recv(1024)

print received # print flag
# No partial derivatives? ;(
'''
Hey, thanks buddy! Here's a little somethin' for your trouble: flag{l3ts_g0_shOpP1ng}
'''
