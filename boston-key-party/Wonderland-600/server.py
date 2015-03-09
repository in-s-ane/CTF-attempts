#!/usr/bin/python

from curve import MODULUS, COEFF_A
from flag import FLAG
## FLAG, rendered with python hex(flag), is the key.  Yes, including the final 'L'

assert(FLAG%4==0)
# Hacks---if you figure out why it is that I need to tell you this, I would
# love to talk about it.  For the mean time, enjoy your two free bits.

def multiply((ax, az), (bx, bz), (dx, dz)):
    res_x = dz*pow((ax-az)*(bx+bz) + (ax+az)*(bx-bz), 2, MODULUS)
    res_z = dx*pow((ax-az)*(bx+bz) - (ax+az)*(bx-bz), 2, MODULUS)
    return res_x % MODULUS, res_z % MODULUS

def square((x, z)):
    res_x = pow(x+z, 2, MODULUS)*pow(x-z, 2, MODULUS)
    res_z = 4*x*z*(pow(x-z, 2, MODULUS) + (COEFF_A+2)*x*z)
    return res_x % MODULUS, res_z % MODULUS

def power(base, power):
    r0 = (1, 0)
    r1 = base
    for bit in bin(power)[2:]:
        if bit == '0':
            r1 = multiply(r0, r1, base)
            r0 = square(r0)
        else:
            r0 = multiply(r0, r1, base)
            r1 = square(r1)
    return r0

def mul_inv(a, b):
    # Thanks, oh internet... far too lazy to write this myself
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def normalize((x, z)):
    return (mul_inv(z, MODULUS) * x) % MODULUS

import base64, SocketServer, os, sys, hashlib

class ServerHandler(SocketServer.BaseRequestHandler):

    def fail(self, message):
        self.request.sendall(message + "\nGood-bye.\n")
        self.request.close()
        return False

    def captcha(self):
        proof = base64.b64encode(os.urandom(9))
        self.request.sendall(proof)
        test = self.request.recv(20)
        ha = hashlib.sha1()
        ha.update(test)
        if test[0:12]!=proof or not ha.digest().endswith('\xFF\xFF'):
            self.fail("You're a robot!")

    def exponentiate(self):
        base = int(self.request.recv(1024))
        result = normalize(power((base, 1), FLAG))
        self.request.sendall(str(result))

    def handle(self):
        self.captcha()
        self.exponentiate()
        self.request.close()


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])

    server = ThreadedServer((HOST, PORT), ServerHandler)
    server.allow_reuse_address = True
    server.serve_forever()
    
