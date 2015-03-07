from binascii import hexlify, unhexlify
import re
import sys

def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def main():
    cipher1 = "f4923a0aa2a3cc07026e38f41b3cd673"
    cipher2 = "8aec78b8dca5541b69d07404f1a6be68"

    x = strxor(unhexlify(cipher1), unhexlify(cipher2))
    print "CRIB DRAG TIME!\n"
    crib = raw_input("Enter crib: ")
    print "Crib: %s\n" % crib


    for i in range(0, len(x)):
        z = x[i:]
        print "\n[%d]" %i
        print "%s"%strxor(z, crib)

main()
